import pytest
import requests
import json
from jsonschema import validate

@pytest.mark.crud
def test_get_all_bookings(api_client,base_url):
 response= api_client.get("/booking")
 assert response.status_code==200
 bookings=response.json()
 assert len(bookings)>0
 assert "bookingid" in bookings[0]

@pytest.mark.crud
def test_single_booking(base_url,create_booking_id):
 response= requests.get(f"{base_url}/booking/{create_booking_id}")
 assert response.status_code==200
 body = response.json()
 assert "firstname" in body
 assert "lastname" in body
 assert "totalprice" in body
 with open("tests/schemas/booking_schema.json") as f:
  schema=json.load(f)
  validate(instance=response.json(),schema=schema)


@pytest.mark.crud
def test_get_booking_filter_by_name(base_url, booking_data,create_booking_id):
  response= requests.get(f"{base_url}/booking", params={"firstname":booking_data["firstname"]})
  assert response.status_code==200
  assert len(response.json())>0

@pytest.mark.crud
def test_get_nonexistent_booking(base_url):
  response= requests.get(f"{base_url}/booking/3232")
  assert response.status_code==404