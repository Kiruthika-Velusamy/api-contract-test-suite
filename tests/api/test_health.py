import allure
import pytest
import requests

@allure.feature("Health Check")
@pytest.mark.smoke
def test_ping(base_url):
    with allure.step("Send GET request to /ping"):
      response=requests.get(f"{base_url}/ping")
    with allure.step("Verify server is alive"):
      assert response.status_code==201

@pytest.mark.smoke
def test_get_all_bookings(base_url):
    with allure.step("Send GET request to /booking"):
      response=requests.get(f"{base_url}/booking")
    with allure.step("Verify bookings returned"):
      assert response.status_code==200
      assert len(response.json())>0

@pytest.mark.smoke
def test_response_time(base_url):
    response=requests.get(f"{base_url}/booking")
    assert response.elapsed.total_seconds()<2.0

