import pytest
import requests

@pytest.mark.smoke
def test_ping(base_url):
    response=requests.get(f"{base_url}/ping")
    assert response.status_code==201

@pytest.mark.smoke
def test_get_all_bookings(base_url):
    response=requests.get(f"{base_url}/booking")
    assert response.status_code==200
    assert len(response.json())>0

@pytest.mark.smoke
def test_response_time(base_url):
    response=requests.get(f"{base_url}/booking")
    assert response.elapsed.total_seconds()<2.0

