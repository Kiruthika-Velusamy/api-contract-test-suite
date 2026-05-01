import pytest
import requests

@pytest.mark.database
def test_api_and_db_consistency(base_url, booking_data, db_helper, auth_token):
    response = requests.post(f"{base_url}/booking",json=booking_data)
    assert response.status_code == 200
    booking_id = response.json()["bookingid"]


    db_helper.insert_booking(booking_id, booking_data)

   
    api_data = requests.get(f"{base_url}/booking/{booking_id}").json()
    db_data = db_helper.get_booking(booking_id)

    assert api_data["firstname"] == db_data[1]
    assert api_data["lastname"] == db_data[2]
    assert api_data["totalprice"] == db_data[3]

    requests.delete(f"{base_url}/booking/{booking_id}",headers={"Cookie": f"token={auth_token}"})
    db_helper.delete_booking(booking_id)


@pytest.mark.database
def test_db_record_exists_after_create(base_url, booking_data, db_helper, auth_token):
    response = requests.post(f"{base_url}/booking",json=booking_data)
    booking_id = response.json()["bookingid"]
    db_helper.insert_booking(booking_id, booking_data)
    db_data = db_helper.get_booking(booking_id)
    assert db_data is not None
    assert db_data[1] == booking_data["firstname"]
    requests.delete(f"{base_url}/booking/{booking_id}",headers={"Cookie": f"token={auth_token}"})
    db_helper.delete_booking(booking_id)


@pytest.mark.database
def test_db_record_deleted_after_api_delete(base_url, booking_data, db_helper, auth_token):
    response = requests.post(f"{base_url}/booking",json=booking_data)
    booking_id = response.json()["bookingid"]
    db_helper.insert_booking(booking_id, booking_data)
    requests.delete(f"{base_url}/booking/{booking_id}",headers={"Cookie": f"token={auth_token}"})
    db_helper.delete_booking(booking_id)
    db_data = db_helper.get_booking(booking_id)
    assert db_data is None
