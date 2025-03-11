from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import PublicRegistrationForm, ProductForm, ReviewForm
from .models import Product,Review
from .models import Category
from django.shortcuts import get_object_or_404

@login_required
def add_product(request):
    if request.user.is_staff:  # Only allow admin users
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.admin = request.user  # Assign product to the logged-in admin
                product.save()
                return redirect('admin_dashboard')  # Redirect to admin dashboard
        else:
            form = ProductForm()
        categories = Category.objects.all()
        return render(request, 'products/add_product.html', {
            'form': form,
            'categories': categories
        })
    else:
        return redirect('home')  # Redirect non-admin users





def public_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # For public login, you might not need to check is_staff.
            login(request, user)
            return redirect('profile')  # Redirect to public profile page
        else:
            messages.error(request, "Invalid credentials. Please try again.")
    return render(request, 'products/public_login.html')
   
def public_register(request):
    if request.method == 'POST':
        form = PublicRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # This creates the new public user
            messages.success(request, "Registration successful! Please log in.")
            # Optionally, you could log the user in automatically:
            # login(request, user)
            # return redirect('profile')
            return redirect('public_login')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = PublicRegistrationForm()
    return render(request, 'products/register.html', {'form': form})


def product_list(request):
    products = Product.objects.all()  # Show all products from all admins
    return render(request, 'products/product_list.html', {'products': products})

@login_required
def profile(request):
    return render(request,"products/profile.html")   


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)  # Get all reviews for this product

    if request.method == "POST":
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.user = request.user
                review.save()
                return redirect('product_detail', product_id=product.id)  # Refresh page after submission
        else:
            return redirect('public_login')  # Redirect to login if user is not logged in
    else:
        form = ReviewForm()

    return render(request, 'products/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form
    })