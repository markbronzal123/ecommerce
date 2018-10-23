from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.product, name='product'),
    path('checkout/', views.checkout, name='checkout'),
    path('signup/', views.signup, name='signup'),
    path('signup/success', views.signupsuccess, name='signupsuccess'),
    path('add-to-cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('delete-cart-item/<int:item_id>', views.delete_cart_item, name='delete_cart_item'),
]
