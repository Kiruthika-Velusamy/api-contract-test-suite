import pytest
import requests
import json
from jsonschema import validate

@pytest.mark.auth
def test_valid_auth(base_url, credentials):
    response = requests.post(f"{base_url}/auth",json={"username":credentials["username"],"password":credentials["password"]})
    assert response.status_code==200
    assert "token" in response.json()
    assert response.json()["token"] !=""
    with open("tests/schemas/auth_schema.json") as f:
     schema=json.load(f)
     validate(instance=response.json(), schema=schema)
    

@pytest.mark.auth
def test_invalid_auth(base_url):
 response= requests.post(f"{base_url}/auth", json={"username":"wrong_user","password":"wrong_password"})
 assert response.status_code==200
 assert response.json()["reason"]=="Bad credentials"
