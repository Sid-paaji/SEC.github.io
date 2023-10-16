from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Homepage
    path('shoes/', views.shoe_list, name='shoe_list'),  # List of shoes
    path('cart/', views.view_cart, name='view_cart'),  # Shopping cart view
    path('login/', views.login_view, name='login'),  # User login view
    path('signup/', views.signup, name='signup'),  # User registration view
    path('logout/', views.logout_view, name='logout'),  # User logout view
    # Add more URL patterns for your other views as needed
]
