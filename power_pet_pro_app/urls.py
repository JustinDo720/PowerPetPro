from django.urls import path, include
from . import views

urlpatterns = [
    # Everything dealing with products will have a product_list prefix (same goes for category with category_list)
    path('', views.index, name='index'),
    path('product_list/', views.ProductList.as_view(), name='product_list'),
    path('category_list/', views.CategoryList.as_view(), name='category_list'),
    path('profile_list/', views.ProfileList.as_view(), name='profile_list'),
    # path('product_detail/<int:product_id>/', views.ProductDetail.as_view(), name='product_detail') ## id format
    # OOOOO so slugs are basically string identifications. You don't need the <int:id> but <slug:string>
    path('product_list/product_detail/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view(), name='product_detail'),
    path('category_list/category_detail/<slug:category_slug>/', views.CategoryDetail.as_view(), name='category_detail'),
    path('product_list/latest_products/', views.LatestProducts.as_view(), name='latest_products'),
    path('product_list/search/', views.search, name='search'),
    path('post_product/', views.PostProduct.as_view(), name='post_product')
]
