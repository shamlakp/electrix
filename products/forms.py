from django import forms
from .models import Product,Category
from .models import Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mptt.forms import TreeNodeChoiceField


class PublicRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProductForm(forms.ModelForm): 
        Category = TreeNodeChoiceField(queryset=Category.objects.all())

        class Meta:
            model = Product
        # Exclude the admin field since it will be set in the view
            fields = ['category', 'name', 'description', 'image']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']
        