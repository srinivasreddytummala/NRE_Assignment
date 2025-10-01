from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from .data import DEVICES_DATA_SAMPLE
from .services import fetch_devices


def devices_api(request):
    """Mock API endpoint returning JSON list of devices."""
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    return JsonResponse(DEVICES_DATA_SAMPLE, safe=False)


def dashboard(request):
    """
    Renders dashboard page by fetching the data from the API endpoint.
    """
    api_url = request.build_absolute_uri("/devices")
    devices = fetch_devices(api_url)
    context = {"devices": devices}
    return render(request, "devices/dashboard.html", context)
