from django.test import Client
from unittest.mock import patch

client = Client()


def test_dashboard_shows_devices_when_fetch_succeeds():
    sample = [{"id": 1, "name": "Router1", "ip_address": "1", "status": "up"}]
    with patch("devices.views.fetch_devices", return_value=sample):
        response = client.get("/")
        assert response.status_code == 200
        content = response.content.decode()
        assert "Router1" in content
        assert "Up" in content


def test_dashboard_shows_warning_on_empty():
    with patch("devices.views.fetch_devices", return_value=[]):
        response = client.get("/")
        assert response.status_code == 200
        assert "No devices found" in response.content.decode()
