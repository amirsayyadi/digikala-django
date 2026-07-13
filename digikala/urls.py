
from django.contrib import admin
from django.urls import path, include
from shop import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.helloword, name= "home"),
    path('about/', views.about, name= "about"),
    path('login/', views.login_user, name= "login"),
    path('logout/', views.logout_user, name= "logout"),
    path('signup', views.signup_user, name= "signup"),
    path('product/<int:pk>', views.product, name= "product"),
    path('categroy/<str:cat>', views.category, name= "category"),
    path('cart/', include('cart.urls')),
    path('category/', views.category_summary, name= "category_summary"),
    path('user_update/', views.user_update, name= "user_update"),
    path('password_update/', views.password_update, name= "password_update"),
    path('info_update/', views.info_update, name= "info_update"),
    path('search/', views.search, name= "search"),
    path('payment/', include('payment.urls')),
    path('orders/', views.user_orders, name= "orders"),
    path('order_details/<int:pk>', views.order_details, name= "order_details"),
   
]


