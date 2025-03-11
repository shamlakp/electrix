
from django.urls import path
from .views import public_login, public_register, product_list,profile,add_product,product_detail

urlpatterns = [
    path("public_login/", public_login, name="public_login"),
    path("register/", public_register, name="public_register"),
    path("product_list/", product_list, name="product_list"),
    path("profile/", profile, name="profile"),
    path("add_product/", add_product, name='add_product'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),

]
