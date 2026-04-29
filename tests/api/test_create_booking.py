import pytest
import requests

@pytest.mark.crud
def test_create_booking(base_url, booking_data):
    response=requests.post(f"{base_url}/booking", json=booking_data)
    assert response.status_code==200
    body = response.json()
    assert "bookingid" in body
    assert body["booking"]["firstname"] == booking_data["firstname"]
    assert body["booking"]["totalprice"] == booking_data["totalprice"]

@pytest.mark.crud
def test_create_booking_returns_id(base_url, booking_data):
    response=requests.post(f"{base_url}/booking", json=booking_data)
    assert response.status_code==200
    assert "bookingid" in response.json()
    booking_id=response.json()["bookingid"]
    assert isinstance(booking_id, int)
    assert booking_id>0


@pytest.mark.parametrize("firstname,lastname,price",[
("Jane", "Doe", 100),
("John", "Smith", 200),
("Alice", "Johnson", 300) ])
def test_create_multiple_bookings(base_url,firstname,lastname,price):
    data={
     "firstname": firstname,
     "lastname": lastname,
     "totalprice": price,
     "depositpaid": True,
     "bookingdates": {
        "checkin": "2026-06-01",
        "checkout": "2026-06-10"
      }
    }
    response=requests.post(f"{base_url}/booking", json =data)
    assert response.status_code==200
    assert response.json()["booking"]["firstname"]==firstname

       

    