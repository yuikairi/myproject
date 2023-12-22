from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('cart/', views.cart, name='cart'), 
    path('camp/', views.camp, name='camp'), 
    path('new/', views.new, name='new'), 
    path('item/', views.item, name='item'), 
    path('detail/<int:product_id>/', views.detail, name='detail'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
]