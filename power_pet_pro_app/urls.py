from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product_list/', views.ProductList.as_view(), name='product_list'),
    path('category_list/', views.CategoryList.as_view(), name='category_list'),
    path('profile_list/', views.ProfileList.as_view(), name='profile_list'),
]
