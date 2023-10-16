from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from .models import Shoe,ShoppingCart
def homepage(request):
    shoes = Shoe.objgitects.all()
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
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page (e.g., homepage)
                return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
def logout_view(request):
    logout(request)
    # Redirect to a specific page after logout (e.g., homepage)
    return redirect('homepage')
def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Redirect to a success page (e.g., homepage)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})