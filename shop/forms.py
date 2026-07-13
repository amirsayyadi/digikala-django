from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms

from .models import Profile



class InfoUpdateForm(forms.ModelForm):

    phone = forms.CharField(
        label= "",
        max_length= 50,
        widget= forms.TextInput(attrs= {"class": "form-control", "placeholder": "تلفن خود را وارد کنید"})
    )

    country = forms.CharField(
        label= "",
        max_length= 50,
        widget= forms.TextInput(attrs= {"class": "form-control", "placeholder": "کشور خود را وارد کنید"})
    )

    city = forms.CharField(
        label= "",
        max_length= 50,
        widget= forms.TextInput(attrs= {"class": "form-control", "placeholder": "شهر خود را وارد کنید"})
    )

    state = forms.CharField(
        label= "",
        max_length= 50,
        widget= forms.TextInput(attrs= {"class": "form-control", "placeholder": "محله خود را وارد کنید"})
    )

    address = forms.CharField(
        label= "",
        max_length= 50,
        widget= forms.TextInput(attrs= {"class": "form-control", "placeholder": "ادرس خود را وارد کنید"})
    )

    zipcode = forms.CharField(
        label= "",
        max_length= 50,
        widget= forms.TextInput(attrs= {"class": "form-control", "placeholder": "کد پستی خود را وارد کنید"})
    )

    class Meta:
        model = Profile
        fields = ['zipcode', 'address', 'state', 'city', 'country', 'phone']




class PasswordUpdateForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label= "",
        widget= forms.PasswordInput(attrs= {"class": "form-control", "name": "password", "type": "password", "placeholder": "رمز عبور خود را وارد کنید"})
    )

    new_password2 = forms.CharField(
        label= "",
        widget= forms.PasswordInput(attrs= {"class": "form-control", "name": "password", "type": "password", "placeholder": "رمز خود را تکرار کنید"})
    )

    class Meta:
        model = User
        fields = ['new_password1', 'new_password1']




class UserUpdateForm(UserChangeForm):
    password = None

    first_name = forms.CharField(
        label= "",
        max_length= 50,
        widget= forms.TextInput(attrs= {"class": "form-control", "placeholder": "نام خود را وارد کنید"})
    )
    
    last_name = forms.CharField(
        label= "",
        max_length= 50,
        widget= forms.TextInput(attrs= {"class": "form-control", "placeholder": "نام خانوادگی خود را وارد کنید"})
    )

    email = forms.EmailField(
        label= "",
        widget= forms.EmailInput(attrs= {"class": "form-control", "placeholder": "ایمیل خود را وارد کنید"})
    )

    username = forms.CharField(
        label= "",
        max_length= 20,
        widget= forms.TextInput(attrs= {"class": "form-control", "placeholder": "نام کاربری خود را وارد کنید"})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']





class SignUpForm(UserCreationForm):

    first_name = forms.CharField(
        label= "",
        max_length= 50,
        widget= forms.TextInput(attrs= {"class": "form-control", "placeholder": "نام خود را وارد کنید"})
    )
    
    last_name = forms.CharField(
        label= "",
        max_length= 50,
        widget= forms.TextInput(attrs= {"class": "form-control", "placeholder": "نام خانوادگی خود را وارد کنید"})
    )

    email = forms.EmailField(
        label= "",
        widget= forms.EmailInput(attrs= {"class": "form-control", "placeholder": "ایمیل خود را وارد کنید"})
    )

    username = forms.CharField(
        label= "",
        max_length= 20,
        widget= forms.TextInput(attrs= {"class": "form-control", "placeholder": "نام کاربری خود را وارد کنید"})
    )

    password1 = forms.CharField(
        label= "",
        widget= forms.PasswordInput(attrs= {"class": "form-control", "name": "password", "type": "password", "placeholder": "رمز عبور خود را وارد کنید"})
    )

    password2 = forms.CharField(
        label= "",
        widget= forms.PasswordInput(attrs= {"class": "form-control", "name": "password", "type": "password", "placeholder": "رمز خود را تکرار کنید"})
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password1", "password2")