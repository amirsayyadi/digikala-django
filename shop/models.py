from django.db import models
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

from django.contrib.auth.models import User

from django.db.models.signals import post_save

class Category(models.Model):
    name = models.CharField(max_length= 20)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length= 20)

    description = models.CharField(max_length= 100,default= '', blank= True, null= True)

    price = models.DecimalField(default= 0, decimal_places= 0, max_digits= 12)

    category = models.ForeignKey(Category, on_delete= models.CASCADE)

    image = models.ImageField()

    is_sale = models.BooleanField(default= False)

    sale_price = models.DecimalField(default= 0, decimal_places= 0, max_digits= 12)

    star = models.IntegerField(default= 0, validators= [MaxValueValidator(5), MinValueValidator(0)])
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)

    date_modified = models.DateTimeField(auto_now= True)

    phone = models.CharField(max_length=25, blank= True)

    country = models.CharField(max_length=25, default= 'IRAN')

    city = models.CharField(max_length=25, blank=True)

    state = models.CharField(max_length=25, blank=True)

    address = models.CharField(max_length=250, blank=True)

    zipcode = models.CharField(max_length=25, blank=True)

    old_cart = models.CharField(max_length= 250, blank= True)

    def __str__(self):
        return self.user.username
    


def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user= instance)
        user_profile.save()


post_save.connect(create_profile, sender= User)