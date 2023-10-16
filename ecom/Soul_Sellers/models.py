from django.db import models
class User(models.Model):
    username=models.CharField(max_length=15,unique=True,null=False)
    f_name=models.CharField(max_length=20)
    l_name=models.CharField(max_length=20)
    email=models.EmailField(unique=True,null=False)
    password=models.CharField(max_length=20,null=False)
    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Shoe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='shoes/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cart = models.ForeignKey('ShoppingCart', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Shoe)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.username}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_seller = models.BooleanField(default=False)
    # Add more fields as needed for user profiles

    def __str__(self):
        return self.user.username

