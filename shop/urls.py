from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path("",views.index,name="ShopHome"),
 
    path("contact",views.contact,name="ContactUs"),
    path("search",views.search,name="search"),
    path("service",views.service,name="service"),
    path("cheackout",views.cheackout,name="cheackout"),
    path("my_account",views.My_account,name="my_account"),
    path("register",views.REGISTER,name="register"),
    path("login",views.login,name="login"),
    path("shop/logout",views.logout,name="logout"),
    path("thanks",views.thanks,name="thanks"),
    path("your_order",views.your_order,name="your_order"),
    path("catview",views.catview,name="catview"),

    path("<str:slug>",views.productView,name="productView"),
  

    #add to cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    
    
]