from django.contrib import admin
from .models import Category, Product, CartItem, MessageBox
from users.models import Profile
from users.models import CustomUser

models = [
    CustomUser,
    CartItem,
    Profile,
    Category,
    Product,
    MessageBox
]
# Register your models here.
for model in models:
    admin.site.register(model)
