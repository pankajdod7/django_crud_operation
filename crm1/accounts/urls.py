from django.urls import path
from accounts.views import home, about

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about")
]
