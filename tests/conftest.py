import shutil
import pytest
import requests
import os
import yaml
from utils.data_factory import generate_booking
from utils.api_client import APIClient
from utils.db_helper import DatabaseHelper



@pytest.fixture
def db_helper():
  db = DatabaseHelper()
  yield db         
  db.close() 

@pytest.fixture
def api_client(base_url, auth_token):
  client=APIClient(base_url)
  client.set_auth_token(auth_token)
  return client

@pytest.fixture(scope="session")
def config():
   config_path = os.path.join(os.path.dirname(__file__),'../config/config.yaml')
   with open(config_path) as f:
     return yaml.safe_load(f)

@pytest.fixture(scope="session")
def base_url(config):
 return config["base_url"]

@pytest.fixture(scope="session")
def credentials(config):
 return config["credentials"]

@pytest.fixture
def auth_token(base_url,credentials):
 response=requests.post(f"{base_url}/auth",json ={
    "username":credentials["username"],
    "password":credentials["password"]
 })
 assert response.status_code==200
 return response.json()["token"]


@pytest.fixture
def booking_data():
  return generate_booking()
    

@pytest.fixture
def create_booking_id(base_url, booking_data,auth_token):
    response=requests.post(f"{base_url}/booking", json=booking_data)
    assert response.status_code==200
    booking_id = response.json()["bookingid"]
    yield booking_id
    requests.delete(f"{base_url}/booking/{booking_id}", headers ={"Cookie" :f"token={auth_token}"})