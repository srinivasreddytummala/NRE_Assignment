from django.urls import path
from . import views

app_name = "devices"

urlpatterns = [
    path("devices", views.devices_api, name="devices-api"),
    path("", views.dashboard, name="dashboard")
]
