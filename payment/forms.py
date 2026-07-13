from django import forms

from .models import ShippingAddress



class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(
        label= "",
        max_length= 50,
        widget= forms.TextInput(attrs= {"class": "form-control", "placeholder": "«نام گیرنده را وارد کنید"}),
        required= True
    )
    shipping_country = forms.CharField(
        label= "",
        max_length= 50,
        widget= forms.TextInput(attrs= {"class": "form-control", "placeholder": " کشور مقصد را وارد کنید"}),
        required= True
    )
    shipping_city = forms.CharField(
        label= "",
        max_length= 50,
        widget= forms.TextInput(attrs= {"class": "form-control", "placeholder": "شهر مقصد را وارد "}),
        required= True
    )
    shipping_state = forms.CharField(
        label= "",
        max_length= 50,
        widget= forms.TextInput(attrs= {"class": "form-control", "placeholder": "محله مقصد را وارد کنید"}),
        required= False
    )
    shipping_address = forms.CharField(
        label= "",
        max_length= 50,
        widget= forms.TextInput(attrs= {"class": "form-control", "placeholder": "ادرس مقصد را وارد کنید"}),
        required= True
    )
    shipping_zipcode = forms.CharField(
        label= "",
        max_length= 50,
        widget= forms.TextInput(attrs= {"class": "form-control", "placeholder": "کد پستی مقصد را وارد کنید"}),
        required= True
    )
    shipping_phone = forms.CharField(
        label= "",
        max_length= 50,
        widget= forms.TextInput(attrs= {"class": "form-control", "placeholder": "تلفن گیرنده را وارد کنید"}),
        required= False
    )

    class Meta:
        model = ShippingAddress
        fields= ['shipping_full_name', 
                  'shipping_country', 
                  'shipping_city', 
                  'shipping_state', 
                  'shipping_address', 
                  'shipping_zipcode', 
                  'shipping_phone'
                ]