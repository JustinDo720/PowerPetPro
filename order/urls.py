from django.urls import path

from order import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('orders/<int:user_id>/', views.UserOrder.as_view(), name='orders'),
    path('latest_orders/<int:user_id>/', views.LatestUserOrder.as_view(), name='latest_orders')
]