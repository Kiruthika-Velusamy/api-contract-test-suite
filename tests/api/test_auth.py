import pytest
import requests

@pytest.mark.auth
def test_valid_auth(base_url, credentials):
    response = requests.post(f"{base_url}/auth",json={"username":credentials["username"],"password":credentials["password"]})
    assert response.status_code==200
    assert "token" in response.json()
    assert response.json()["token"] !=""

@pytest.mark.auth
def test_invalid_auth(base_url):
 response= requests.post(f"{base_url}/auth", json={"username":"wrong_user","password":"wrong_password"})
 assert response.status_code==200
 assert response.json()["reason"]=="Bad credentials"
