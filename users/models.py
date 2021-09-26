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
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    email = models.EmailField(max_length=250, unique=True, blank=False, null=False)

    objects = UserAccountManager()
