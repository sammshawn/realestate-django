from django.urls import path
from . import views


app_name = "listings"

urlpatterns = [
    path("", views.home, name="home"),
    path("properties/", views.property_list, name="property_list"),
    path("properties/<int:pk>/", views.property_detail, name="property_detail"),
]