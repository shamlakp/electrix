from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AdminRegistrationForm


#electronic product review


def admin_login(request):
    """
    Handles admin login. Authenticates the user and checks if they are staff.
    If successful, logs in and redirects to the admin dashboard.
    Otherwise, shows an error message.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard')  # Make sure the URL name 'dashboard' is correctly defined.
        else:
            messages.error(request, "Invalid credentials or you do not h"
            "ave admin access.")
            print("DEBUG:Login failed")
    return render(request, "accounts/admin_login.html")


def admin_register(request):
    """
    Handles admin registration using AdminRegistrationForm.
    Upon successful registration, marks the user as staff and either redirects to the login page 
    or renders the registration page with a success flag (for popup modal).
    """
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = True  # Mark the user as an admin.
            user.save()
            messages.success(request, "Registration successful!")
            # Option 1: Redirect to admin login page after registration.
            return redirect('admin_login')
            # Option 2: Render the registration page with a success flag for a popup modal.
            # return render(request, "accounts/register.html", {'registration_success': True})
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = AdminRegistrationForm()
    return render(request, "accounts/register.html", {'form': form})

@login_required
def dashboard(request):
    """
    Displays the admin dashboard with products belonging to the logged-in admin.
    Assumes that the Product model has a ForeignKey to the User with related_name='products'.
    """
    # Retrieve products associated with the logged-in admin.
    products = request.user.products.all() if hasattr(request.user, 'products') else []
    context = {
        'admin': request.user,
        'products': products,
    }
    return render(request, "accounts/dashboard.html", context)

