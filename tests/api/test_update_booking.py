import pytest
import requests

@pytest.mark.crud
def test_put_booking(base_url,create_booking_id,auth_token):
   updated = {
    "firstname": "Updated",
    "lastname": "User",
    "totalprice": 999,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2026-08-01",
        "checkout": "2026-08-10"
        }
    }
   response=requests.put(f"{base_url}/booking/{create_booking_id}",json=updated, headers={"Cookie" : f"token ={auth_token}"})
   assert response.status_code==200
   assert response.json()["firstname"]==updated["firstname"]
   assert response.json()["lastname"]==updated["lastname"]

@pytest.mark.crud
def test_patch_booking(base_url,create_booking_id,auth_token):
   response=requests.patch(f"{base_url}/booking/{create_booking_id}",json={"firstname":"Patched"}, headers={"Cookie" : f"token ={auth_token}"})
   assert response.status_code==200
   assert response.json()["firstname"]=="Patched"
 
@pytest.mark.crud
def test_patch_without_auth(base_url,create_booking_id):
   response=requests.patch(f"{base_url}/booking/{create_booking_id}",json={"firstname":"No auth"})
   assert response.status_code==403
   
 