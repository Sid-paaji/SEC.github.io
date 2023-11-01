from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from django.http import HttpResponse
from .models import Shoe,ShoppingCart
def homepage(request):
    shoes = Shoe.objects.all()
    return render(request, 'home.html',{'shoes':shoes})
def shoe_list(request):
    shoes = Shoe.objects.all()
    return render(request, 'shoes/shoe_list.html', {'shoes': shoes})
def view_cart(request):
    user = request.user  # Assuming you're using Django's built-in authentication
    cart = ShoppingCart.objects.filter(user=user).first()
    return render(request, 'cart/view_cart.html', {'cart': cart})
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        return HttpResponse('no login')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
def logout_view(request):
    logout(request)
    # Redirect to a specific page after logout (e.g., homepage)
    return redirect('homepage')
def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        username=form.cleaned_data.get('username')
        fname=form.cleaned_data.get('first_name')
        lname=form.cleaned_data.get('last_name')
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        
        if form.is_valid():
            user=User.objects.create_user()
            user.username=username
            user.first_name=fname
            user.last_name=lname
            user.email=email
            user.password=password
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
        return render(request, 'signup.html', {'form': form})