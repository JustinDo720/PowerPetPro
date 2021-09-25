from django.contrib import admin
from .models import Profile, Category, Product
from users.models import CustomUser

models = [
    CustomUser,
    Profile,
    Category,
    Product
]
# Register your models here.
for model in models:
    admin.site.register(model)
