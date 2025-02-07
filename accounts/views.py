from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib import messages
from rest_framework import generics
from .serializers import *

# Create your views here.

# ListCreateAPIView provides GET (list) and POST (create) actions

class ProductsListCreate(generics.ListCreateAPIView):
    queryset = tblProducts.objects.all()    
    serializer_class = ProductSerializer


class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = tblProducts.objects.all()
    serializer_class = ProductSerializer

# ============ Category =============
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()    
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# ============ Sildes =============
class SildesListCreate(generics.ListCreateAPIView):
    queryset = tblSlides.objects.all()    
    serializer_class = SildesSerializer

class SildesDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = tblSlides.objects.all()
    serializer_class = SildesSerializer

# ============ SupTopMenu =============
class SubTopMenuListCreate(generics.ListCreateAPIView):
    queryset = tblSubTopMenu.objects.all()    
    serializer_class = SubTopMenuSerializer

class SubTopMenuDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = tblSubTopMenu.objects.all()
    serializer_class = SubTopMenuSerializer

# ============ TopMenu =============
class TopMenuListCreate(generics.ListCreateAPIView):
    queryset = tblTopMenu.objects.all()    
    serializer_class = TopMenuSerializer

class TopMenuDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = tblTopMenu.objects.all()
    serializer_class = TopMenuSerializer
########## end API views ##########

def index(request):
    SocialMedia = tblSocialMedia.objects.all 
    Product = tblProducts.objects.all
    Categorie = Category.objects.all
    Slide = tblSlides.objects.all 
    TopMenu = tblTopMenu.objects.all
    SubTopMenu = tblSubTopMenu.objects.all

    cart = Cart.objects.get(user=request.user)
    cart_items = cart.items.all()

    subtotal = sum(float(item.product.current_price) * int(item.quantity) for item in cart_items)
    grand_total = subtotal

    context = {
        'SocialMedias':SocialMedia,
        'Products':Product,
        'Categories':Categorie,
        'Slides':Slide,
        'TopMenus':TopMenu,
        'SubTopMenus':SubTopMenu,
        'cart_items': cart_items,
        'subtotal': subtotal,
        'grand_total': grand_total,
        
    }
    return render(request,'accounts/index.html',context)

def shop(request):
    TopMenu = tblTopMenu.objects.all
    SubTopMenu = tblSubTopMenu.objects.all
    
    context = {        
        'TopMenus':TopMenu,
        'SubTopMenus':SubTopMenu,
     }
    return render(request,'accounts/shop.html',context)
     
def Product(request):
    TopMenu = tblTopMenu.objects.all
    SubTopMenu = tblSubTopMenu.objects.all
    Product = tblProducts.objects.all
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.items.all()

    subtotal = sum(float(item.product.current_price) * int(item.quantity) for item in cart_items)
    grand_total = subtotal
    context = {
        'TopMenus':TopMenu,
        'SubTopMenus':SubTopMenu,
        'Products':Product,
        'cart_items': cart_items,
        'subtotal': subtotal,
        'grand_total': grand_total,
     }
    return render(request, "accounts/Product.html",context)

def pages(request):
    TopMenu = tblTopMenu.objects.all
    SubTopMenu = tblSubTopMenu.objects.all
    
    context = {        
        'TopMenus':TopMenu,
        'SubTopMenus':SubTopMenu,
     }
    return render(request,'accounts/pages.html',context)
     
def blog(request):
    TopMenu = tblTopMenu.objects.all
    SubTopMenu = tblSubTopMenu.objects.all
    
    context = {        
        'TopMenus':TopMenu,
        'SubTopMenus':SubTopMenu,
     }
    return render(request,'accounts/blog.html',context)

def product_details(request):
    TopMenu = tblTopMenu.objects.all
    SubTopMenu = tblSubTopMenu.objects.all
    
    context = {        
        'TopMenus':TopMenu,
        'SubTopMenus':SubTopMenu,
     }
    return render(request,'accounts/product-details.html',context)

def CartPage(request):
    TopMenu = tblTopMenu.objects.all
    SubTopMenu = tblSubTopMenu.objects.all
    
    context = {        
        'TopMenus':TopMenu,
        'SubTopMenus':SubTopMenu,
     }
    return render(request,'accounts/CartPage.html',context)


def mini_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.items.all()
    cart_total = sum(item.total_price for item in cart_items)

    subtotal = sum(float(item.product.current_price) * int(item.quantity) for item in cart_items)
    grand_total = subtotal
    context ={
        'cart_items': cart_items,
        'cart_total': cart_total,
        'subtotal': subtotal,
        'grand_total': grand_total,
    }
    return render(request, 'path/miniCart.html', context)

# @login_required
def cart_view(request):
    TopMenu = tblTopMenu.objects.all
    SubTopMenu = tblSubTopMenu.objects.all
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    
    # Ensure all values are numeric
    subtotal = sum(float(item.product.current_price) * int(item.quantity) for item in cart_items)
    grand_total = subtotal

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'grand_total': grand_total,
        'TopMenus':TopMenu,
        'SubTopMenus':SubTopMenu,

    }
    return render(request, 'accounts/cart.html', context)

def add_to_cart(request, product_id):
    product = tblProducts.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Create or update CartItem
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'price': float(product.current_price), 'quantity': 1}
    )  
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('view_cart')

def update_cart(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('quantity_'):
                item_id = key.split('_')[1]
                cart_item = get_object_or_404(CartItem, id=item_id)
                cart_item.quantity = int(value)
                cart_item.save()
    return redirect('view_cart')


def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('view_cart')

def clear_cart(request):
    if request.method == 'POST':
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart.items.all().delete()  # Clear all items in the cart
        return JsonResponse({'status': 'success', 'message': 'Cart cleared successfully!'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

def cart_item_count(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            return {'cart_item_count': cart.items.count(0)}
    return {'cart_item_count': 0}
# end cart

#Checkout
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    TopMenu = tblTopMenu.objects.all
    SubTopMenu = tblSubTopMenu.objects.all
    # Calculate total_price for each item dynamically
    for item in cart_items:
        if item.price is None:
            item.price = 0
        item.total_price = item.price * item.quantity

    # Calculate cart_total
    cart_total = sum(item.total_price for item in cart_items)

    if request.method == 'POST':
        # Create an order
        order = Order.objects.create(
            user=request.user,
            cart=cart,
            total_amount=cart_total,
            shipping_address=request.POST.get('address'),
            status='Pending'
        )

        # Clear the cart
        cart.items.all().delete()

        # messages.success(request, 'Your order has been placed successfully!')
        return redirect('order_confirmation', order_id=order.id)

    return render(request, 'accounts/checkout.html', {
        'cart_items': cart_items,
        'cart_total': cart_total,
        'TopMenus':TopMenu,
        'SubTopMenus':SubTopMenu,
    })

def place_order(request):
    if request.method == 'POST':
        # Get the current user's cart
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.all()
        cart_total = sum(item.total_price for item in cart_items)

        # Create an order
        order = Order.objects.create(
            user=request.user,
            cart=cart,
            total_amount=cart_total,
            shipping_address=request.POST.get('address'),
            city=request.POST.get('city'),
            country=request.POST.get('country'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            payment_method=request.POST.get('payment_method'),
            status='Pending'
        )

        # Clear the cart after placing the order
        cart.items.all().delete()

        # Redirect to an order confirmation page
        messages.success(request, 'Your order has been placed successfully!')
        return redirect('order_confirmation', order_id=order.id)

    # If the request is not POST, redirect to the checkout page
    return redirect('checkout')
# def place_order(request):
    if request.method == 'POST':
        try:

            cart = Cart.objects.get(user=request.user)
            cart_items = cart.items.all()  # ✅ Use the correct related_name
            
            if not cart_items.exists():
                return JsonResponse({"error": "Your cart is empty!"}, status=400)

            # ✅ Calculate total amount
            total_amount = sum(item.quantity * item.product.current_price for item in cart_items)

            # ✅ Create a new order
            order = Order.objects.create(
                user=request.user,
                cart=cart,  # ✅ Linking cart to order
                total_amount=total_amount,
                shipping_address=request.POST.get('address'),
                status='Pending'
            )

            # ✅ Copy cart items to OrderItem before deleting
            for item in cart_items:
                Order.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.current_price
                )

            # ✅ Clear CartItems after Order is placed
            cart_items.delete()  # ✅ This should remove all cart items

            messages.success(request, 'Your order has been placed successfully!')
            return JsonResponse({"success": "Order placed!", "redirect_url": f"/order-confirmation/{order.id}/"})
        
        except Cart.DoesNotExist:
            return JsonResponse({"error": "Cart not found!"}, status=400)

    return redirect('checkout')


def blog_details(request):
     return render(request, "accounts/blog-details.html")


def ListCategory(request):
    category = Category.objects.all()
    context = {
        'categorys' :category,
    }
    return render(request, 'accounts/ListCategory.html', context)

