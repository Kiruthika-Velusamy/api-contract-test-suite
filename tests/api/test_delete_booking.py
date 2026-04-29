import pytest
import requests

@pytest.mark.crud
def test_delete_booking(base_url, booking_data, auth_token):
 create_response=requests.post(f"{base_url}/booking", json=booking_data)
 assert create_response.status_code==200
 booking_id = create_response.json()["bookingid"]

 delete_response=requests.delete(f"{base_url}/booking/{booking_id}",headers ={"Cookie" : f"token ={auth_token}"})
 assert delete_response.status_code==201

 get_response= requests.get(f"{base_url}/booking/{booking_id}")
 assert get_response.status_code==404

@pytest.mark.crud
def test_delete_without_auth(base_url, create_booking_id):
 response=requests.delete(f"{base_url}/booking/{create_booking_id}")
 assert response.status_code==403