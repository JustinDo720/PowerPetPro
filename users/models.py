from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import Q


class UserAccountManager(UserManager):

    # so here get_by_natural_key takes in either username or email but make sure to use "username" as key when posting
    def get_by_natural_key(self, username):
        return self.get(
            Q(**{self.model.USERNAME_FIELD: username}) |
            Q(**{self.model.EMAIL_FIELD: username})
        )


# Create your models here.
class CustomUser(AbstractUser):
    username = models.TextField(max_length=250, unique=True, blank=False, null=False)
    email = models.EmailField(max_length=250, unique=True, blank=False, null=False)

    objects = UserAccountManager()


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.TextField(max_length=100, blank=True, null=True)
    last_name = models.TextField(max_length=100, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    address = models.TextField(max_length=100, blank=True, null=True)
    city = models.TextField(max_length=100, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)
    country = models.TextField(max_length=75, blank=True, null=True)
    state = models.TextField(max_length=75, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
