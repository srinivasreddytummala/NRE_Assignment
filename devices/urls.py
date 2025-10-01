from django.urls import path
from . import views

app_name = "device"

urlpatterns = [
    path("devices", views.devices_api),
    path("", views.dashboard)
]
