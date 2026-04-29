import requests

BASE_URL = "https://restful-booker.herokuapp.com"
response = requests.get(f"{BASE_URL}/booking")
print(response.json()[0]['bookingid']) 
print(response.text)
print(response.headers)
print(response.status_code)



#Filter by Nmae - Get with query parameter
print("------------------Query Param--------------")
response = requests.get(f"{BASE_URL}/booking", params={"firstname":"Jim"})
print(response.json()) 
print(response.status_code) 



#POST - create booking
print("------------------POST - Create booking--------------")
new_booking = {
    "firstname": "Kiruthika",
    "lastname": "Velusamy",
    "totalprice": 200,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2026-06-01",
        "checkout": "2026-06-10"
    },
    "additionalneeds": "Breakfast"
}

response=requests.post(f"{BASE_URL}/booking", json=new_booking)
print(response.json()) 
print(response.status_code) 


#Get Auth token
print("------------Get Auth token----------------")
auth_response=requests.post(f"{BASE_URL}/auth",json ={"username": "admin","password": "password123"})
token=auth_response.json()["token"]
print(f"Token is: {token}")

#PUT(Full Update)
print("------------PUT---------------")
updated_booking = {
    "firstname": "Updated",
    "lastname": "User",
    "totalprice": 999,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2026-07-01",
        "checkout": "2026-07-10"
    }
}

response = requests.put(f"{BASE_URL}/booking/1",json=updated_booking,headers={"Cookie": f"token={token}"})
print(response.status_code)
print(response.json())

#PATCH(Partial Update)
print("------------PATCH---------------")
response=requests.patch(f"{BASE_URL}/booking/1",json={"firstname":"Patched"}, headers={"Cookie":f"token={token}"})
print(response.status_code)
print(response.json())

# DELETE — remove booking
print("------------DELETE---------------")
response = requests.delete(f"{BASE_URL}/booking/1",headers={"Cookie": f"token={token}"})
print(response.status_code)  # 201


#Session object
session=requests.Session()
session.headers.update({"Content-Type":"application/json","Cookie":f"token={token}"})
# Now every request uses these headers automatically
response = session.get(f"{BASE_URL}/booking/2")
print(response.json())

response = session.get(f"{BASE_URL}/booking/3")
print(response.json())
