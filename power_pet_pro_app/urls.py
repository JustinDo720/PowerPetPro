from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

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
    path('admin_panel/post_product/', views.PostProduct.as_view(), name='post_product'),
    path('admin_panel/product_list/update/<int:product_id>/', views.updateProduct, name='update_product'),
    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('activate/<str:uid>/<str:token>/', views.activate_acc, name='activate_acc'),
    path('password/reset/confirm/<str:uid>/<str:token>/', views.reset_password, name='reset_password'),
    path('profile_list/user_profile/<int:user_id>/', views.UserProfile.as_view(), name='user_profile'),
    path('profile_list/user_profile/<int:user_id>/cart/', views.UserCart.as_view(), name='user_cart'),
    path('profile_list/user_profile/<int:user_id>/cart/<int:product_id>/', views.updateUserCart, name='update_user_cart'),
    path('admin_panel/message_box/', views.MessageBoxView.as_view(), name='message_box'),
    path('admin_panel/message_bar/', views.MessageBarView.as_view(), name='message_bar'),
    path('admin_panel/message_box/update/<int:message_id>/', views.updateMessageBoxView, name='update_msg_box_view'),
    path('admin_panel/message_box/post/', views.postMessageBoxView, name='post_msg_box_view'),
    path('admin_panel/post_category/', views.PostCategory.as_view(), name='post_category'),
]
