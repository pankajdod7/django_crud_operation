from django.urls import path
from accounts.views import home, products, customer

urlpatterns = [
    path("", home, name="dashboard"),
    path("products/", products, name="products"),
    path("customers/", customer, name="customer"),
]
