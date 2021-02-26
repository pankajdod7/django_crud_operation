from django.urls import path
from accounts.views import home, products, customer, createOrder, updateOrder, deleteOrder

urlpatterns = [
    path("", home, name="home"),
    path("products/", products, name="products"),
    path("customers/<str:pk_test>/", customer, name="customer"),
    path("create_order/<str:pk>/", createOrder, name="create_order"),
    path("update_order/<str:pk>/", updateOrder, name="update_order"),
    path("delete_order/<str:pk>/", deleteOrder, name="delete_order"),

]
