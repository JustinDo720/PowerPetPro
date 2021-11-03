from django.contrib import admin
from .models import Category, Product, CartItem, MessageBox, MissionStatement, MissionStatementTopics, MissionDetails
from users.models import Profile
from users.models import CustomUser

models = [
    CustomUser,
    CartItem,
    Profile,
    Category,
    Product,
    MessageBox,
    MissionStatement,
    MissionStatementTopics,
    MissionDetails,
]
# Register your models here.
for model in models:
    admin.site.register(model)
