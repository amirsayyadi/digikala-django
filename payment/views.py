from django.shortcuts import render, redirect, get_object_or_404

from cart.cart import Cart

from .models import ShippingAddress, Order, OrderItem
from .forms import ShippingForm

from django.contrib import messages

from shop.models import Product, Profile

from django.contrib.auth.models import User



def process_order(request):
    if request.POST:
        
        user_shipping = request.session.get('user_shipping')

        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        total = cart.get_total()

        full_name = user_shipping['shipping_full_name']
        phone = user_shipping['shipping_phone']
        shipping_address = f"{user_shipping['shipping_country']} \n {user_shipping['shipping_city']} \n {user_shipping['shipping_state']} \n {user_shipping['shipping_address']} \n {user_shipping['shipping_zipcode']} "

        if request.user.is_authenticated:
            user = request.user
            new_order = Order(
                user=user,
                full_name=full_name,
                phone=phone,
                shipping_address=shipping_address,
                amount_paid=total
            )
            new_order.save()

            odr = get_object_or_404(Order, id= new_order.pk)

            for product in cart_products:
                prod = get_object_or_404(Product, id= product.id)

                if product.is_sale:
                    price = prod.sale_price
                else:
                    price = prod.price

                for k, v in quantities.items():
                    if int(k) == prod.id:
                        new_item = OrderItem(
                            user = user,
                            order = odr,
                            product= prod,
                            price = price,
                            quantity = v
                        )
                new_item.save()
            
            for key in list(request.session.keys()):
                if key == 'session_key':
                    del request.session['session_key']

            user_profile = Profile.objects.filter(user__id= request.user.id)
            user_profile.update(old_cart= "")
            
            messages.success(request, ' سفارش با موفقیت ثبت شد ')
            return redirect('home')
        else:
            new_order = Order(
                full_name=full_name,
                phone=phone,
                shipping_address=shipping_address,
                amount_paid=total
            )
            new_order.save()

            odr = get_object_or_404(Order, id= new_order.pk)

            for product in cart_products:
                prod = get_object_or_404(Product, id= product.id)

                if product.is_sale:
                    price = prod.sale_price
                else:
                    price = prod.price

                for k, v in quantities.items():
                    if int(k) == prod.id:
                        new_item = OrderItem(
                            order = odr,
                            product= prod,
                            price = price,
                            quantity = v
                        )
                new_item.save()
            for key in list(request.session.keys()):
                if key == 'session_key':
                    del request.session['session_key']
        

            messages.success(request, ' سفارش با موفقیت ثبت شد ')
            return redirect('home')

    else:
        messages.success(request, ' دسترسی به این صفحه امکان پذیر نمی باشد ')
        return redirect('home')




def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    total = cart.get_total()

    if request.user.is_authenticated:
        user_shipping = ShippingAddress.objects.get(user__id= request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance= user_shipping)
        return render(request, 'checkout.html', {'cart_products': cart_products, 'quantities': quantities, 'total': total, 'shipping_form': shipping_form})
    else:
        shipping_form = ShippingForm(request.POST or None)
        return render(request, 'checkout.html', {'cart_products': cart_products, 'quantities': quantities, 'total': total, 'shipping_form': shipping_form})
    

def confirm_order(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        total = cart.get_total()

        shipping_form = request.POST
        request.session['user_shipping'] = shipping_form
        
        return render(request, 'confirm_order.html', {'cart_products': cart_products, 'quantities': quantities, 'total': total, 'shipping_form': shipping_form})

    else:
        messages.success(request, ' دسترسی به این صفحه امکان پذیر نمی باشد ')
        return redirect('home')


    