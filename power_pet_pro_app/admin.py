from django.contrib import admin
from .models import Category, Product, MessageBox, MissionStatement, MissionStatementTopics, MissionDetails
from order.models import CartItem, Order
from users.models import Profile
from users.models import CustomUser

models = [
    CustomUser,
    Order,
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
