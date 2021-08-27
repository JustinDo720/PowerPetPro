from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product_list/', views.ProductList.as_view(), name='product_list'),
    path('category_list/', views.CategoryList.as_view(), name='category_list'),
    path('profile_list/', views.ProfileList.as_view(), name='profile_list'),
    # path('product_detail/<int:product_id>/', views.ProductDetail.as_view(), name='product_detail') ## id format
    # OOOOO so slugs are basically string identifications. You don't need the <int:id> but <slug:string>
    path('product_detail/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view(), name='product_detail'),
    path('category_detail/<slug:category_slug>/', views.CategoryDetail.as_view(), name='category_detail'),
]
