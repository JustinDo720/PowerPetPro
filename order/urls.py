from django.urls import path

from order import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('profile/<int:user_id>/orders/', views.UserOrder.as_view(), name='orders'),
    path('latest_orders/<int:user_id>/', views.LatestUserOrder.as_view(), name='latest_orders'),
    path('profile/<int:user_id>/order/<int:order_id>/', views.IndividualUserOrder.as_view(), name='orders'),
    path('profile/<int:user_id>/order/<int:order_id>/items/', views.IndividualUserOrderItems.as_view(), name='orders'),
]