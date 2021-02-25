from django.urls import path
from accounts.views import home, products, customer

urlpatterns = [
    path("", home, name="home"),
    path("products/", products, name="products"),
    path("customers/<str:pk_test>/", customer, name="customer"),
]
