from django.urls import path
from . import views
from .views import *
# from .views import update_cart, add_to_cart, remove_from_cart, clear_cart, view_cart

urlpatterns = [

    path('', views.index, name='index'),
    path('Home', views.index, name='index'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path('Blog', views.blog, name='blog'),
    path('CartPage/', views.CartPage, name='CartPage'),


    path('cart', views.cart_view, name='cart'),
    path('cart/', views.cart_view, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout', views.checkout, name='checkout'),

    path('product_details/', views.product_details, name='product_details'),
    path('shop/', views.shop, name='shop'),
    path('showCategory/', views.ListCategory, name= 'categorys'),
    # path('ViewBlog/<int:pk>', views.ViewBlog, name='ViewBlog'),
    path('pages/', views.pages, name='pages'),
    path('Product', views.Product, name='Product'),
 
    path('mini-cart/', views.mini_cart, name='mini_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/', views.update_cart, name='update_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('clear-cart/', views.clear_cart, name='clear_cart'),
    path('place-order/', views.place_order, name='place_order'),

    #api    
    path('Pros/', ProductsListCreate.as_view(), name='ProList'),
    path('Pros/<int:pk>/', ProductsDetail.as_view(), name='ProDetail'),
    
    path('Category/', CategoryListCreate.as_view(), name='CategoryList'),
    path('Category/<int:pk>/', CategoryDetail.as_view(), name='CategoryDetail'),
    path('Sildes/', SildesListCreate.as_view(), name='SildesList'),
    path('Sildes/<int:pk>/', SildesDetail.as_view(), name='SildesDetail'),

    path('SubTopMenu/', SubTopMenuListCreate.as_view(), name='SubTopMenuList'),
    path('SubTopMenu/<int:pk>/', SubTopMenuDetail.as_view(), name='SubTopMenuDetail'),

    path('TopMenu/', TopMenuListCreate.as_view(), name='TopMenuList'),
    path('TopMenu/<int:pk>/', TopMenuDetail.as_view(), name='TopMenuDetail'),

]