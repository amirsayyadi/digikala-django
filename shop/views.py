from django.shortcuts import render, HttpResponse
from .models import Product, Category, Profile

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UserUpdateForm, PasswordUpdateForm, InfoUpdateForm

from django.db.models import Q

from cart.cart import Cart

from .models import Profile

import json

from payment.models import ShippingAddress, Order, OrderItem
from payment.forms import ShippingForm



def order_details(request, pk):
    order = Order.objects.get(id= pk)

    if request.user.is_authenticated and request.user == order.user:
        items = OrderItem.objects.filter(order= pk)

        context = {
            'order': order,
            'items': items
        }


        return render(request, 'order_details.html', context)
    

    else:
        messages.success(request, ' ابتدا لاگین کنید ')
        return redirect('login')



def user_orders(request):
    if request.user.is_authenticated:
        delivered_orders = Order.objects.filter(user= request.user, status= 'Delivered')
        other_orders = Order.objects.filter(user= request.user).exclude(status= 'Delivered')

        context = {
            'delivered' : delivered_orders,
            'other' : other_orders
        }



        return render(request, 'orders.html', context)
    

    else:
        messages.success(request, ' ابتدا لاگین کنید ')
        return redirect('login')




def helloword(request):
    
    all_products = Product.objects.all()
    
    return render(request, 'index.html', {'products' : all_products})


def about(request):
    return render(request, 'about.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)

            user_profile = Profile.objects.get(user__id= user.id)
            old_cart = str(user_profile.old_cart)
            

            if old_cart:
                converted_cart = json.loads(str(user_profile.old_cart))
                cart = Cart(request)
                for key, value in converted_cart.items():
                    cart.db_add(product= key, quantity= value)

            messages.success(request, ("با موفقیت وارد شدید"))
            return redirect("home")
        else:
            messages.success(request, ("مشکلی در لاگین وجود داشت"))
            return redirect("login")

    else:

        return render(request, 'login.html')


def logout_user(request):

    logout(request)

    messages.success(request, ("با موفقیت خارج شدید"))
    
    return redirect("home")


def signup_user(request):

    form = SignUpForm()
    
    if request.method == "POST":

        form = SignUpForm(request.POST)

        if form.is_valid():

            form.save()

            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']

            user= authenticate(request, username= username, password= password1)

            login(request, user)
            messages.success(request, ("ثبت نام موفقیت امیز بود"))

            return redirect('home')
        
        else:
            messages.success(request, ("مشکلی در ثبت نام وجود داشت"))
            return redirect('signup')

    else:
        return render(request, 'signup.html', {"form": form})
    

def product(request, pk):

    product = Product.objects.get(id= pk)

    return render(request, 'product.html', {'product': product})


def category(request, cat):
    try:
        category = Category.objects.get(name= cat)
        products = Product.objects.filter(category= category)

        return render(request, 'category.html', {'products': products, 'category': category})
    except:
        messages.success(request, (' دسته بندی وجود ندارد '))

        return redirect("home")
    

def category_summary(request):

    all_cat = Category.objects.all()

    return render(request, 'category_summary.html', {'category': all_cat})




def user_update(request):
    if request.user.is_authenticated:
        current_user = request.user
        user_shipping = ShippingAddress.objects.get(user__id= current_user.id)

        form = UserUpdateForm(request.POST or None, instance= current_user)
        shipping_form = ShippingForm(request.POST or None, instance= user_shipping)
        

        if form.is_valid() and shipping_form.is_valid():
            form.save()
            shipping_form.save()
            
            login(request, current_user)

            messages.success(request, ' پروفایل کاربری شما ویرایش شد ')
            return redirect('home')

        return render(request, 'user_update.html', {'form': form, 'shipping_form': shipping_form})
    else:
        messages.success(request, ' ابتدا لاگین کنید ')
        return redirect('login')
    

def password_update(request):
    if request.user.is_authenticated:
        user = User.objects.get(id= request.user.id)
 
        if request.method == "POST":
            form = PasswordUpdateForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, (' رمز با موفقیت ویرایش شد '))
                login(request, user)
                return redirect('user_update')
            
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

                return redirect('password_update')
        else:
            form = PasswordUpdateForm(user)
            return render(request, 'password_update.html', {'form': form})

    else:
        messages.success(request, (' ابتدا باید وارد شوید '))
        return redirect('login')



def info_update(request):
    if request.user.is_authenticated:
        current_user = request.user
        user_profile = Profile.objects.get(user__id= current_user.id)
        form = InfoUpdateForm(request.POST or None, instance= user_profile)

        if form.is_valid():
            form.save()

            messages.success(request, ' اطلاعات کاربری شما ویرایش شد ')
            return redirect('home')

        return render(request, 'info_update.html', {'form': form})
    else:
        messages.success(request, ' ابتدا لاگین کنید ')
        return redirect('login')
    



def search(request):
    if request.method == "POST":
        searched = request.POST['search']
        searched = Product.objects.filter(Q(name__icontains= searched)|Q(description__icontains= searched))
        return render(request, 'search.html', {'searched': searched})
    return render(request, 'search.html')