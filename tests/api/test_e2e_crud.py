import pytest
import requests

class TestBookingCRUD:

    def test_01_create_booking(self,base_url,booking_data):
        response=requests.post(f"{base_url}/booking", json=booking_data)
        assert response.status_code==200
        assert "bookingid" in response.json()
        TestBookingCRUD.booking_id =response.json()["bookingid"]

    def test_02_read_booking(self,base_url):
        response = requests.get(f"{base_url}/booking/{self.booking_id}")
        assert response.status_code==200
        assert response.json()["firstname"] is not None

    def test_03_update_booking(self,base_url,auth_token):
        updated={
                "firstname": "Updated",
                "lastname": "User",
                "totalprice": 999,
                "depositpaid": True,
                "bookingdates": {
                    "checkin": "2026-08-01",
                    "checkout": "2026-08-10"
                }
        }
        response = requests.put(f"{base_url}/booking/{self.booking_id}", json=updated, headers={"Cookie": f"token={auth_token}"})
        assert response.json()["firstname"]=="Updated"


    def test_04_delete_booking(self,base_url,auth_token):
        response = requests.delete(f"{base_url}/booking/{self.booking_id}",headers={"Cookie": f"token={auth_token}"})
        assert response.status_code==201

    def test_05_verify_delete_booking(self,base_url):
        response = requests.get(f"{base_url}/booking/{self.booking_id}")
        assert response.status_code==404