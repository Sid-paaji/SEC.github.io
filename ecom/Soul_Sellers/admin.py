from django.contrib import admin
from .models import User,Category,Shoe,ShoppingCart,UserProfile
admin.site.register(User)
admin.site.register(Shoe)
admin.site.register(ShoppingCart)
admin.site.register(UserProfile)
admin.site.register(Category)


# Register your models here.
