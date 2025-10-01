import json
from django.test import Client

client = Client()


def test_devices_api_get_returns_sample_list():
    response = client.get("/devices")
    assert response.status_code == 200
    data = json.loads(response.content)
    assert isinstance(data, list)
    # check a couple of expectations from the sample data list
    assert any(d.get("name") == "Router1" for d in data)
    assert any(d.get("status") in ("Up", "Down") for d in data)


def test_devices_api_wrong_method_returns_405():
    response = client.post("/devices", {})
    assert response.status_code == 405
