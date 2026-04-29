import random
import string

def generate_booking() ->dict:
 random_str = ''.join(
        random.choices(string.ascii_lowercase, k=5)
    )
 return{
        "firstname": f"Test{random_str}",
        "lastname": f"User{random_str}",
        "totalprice": random.randint(50, 500),
        "depositpaid": random.choice([True, False]),
        "bookingdates": {
            "checkin": "2026-07-01",
            "checkout": "2026-07-10"
        },
        "additionalneeds": "Breakfast"
    }
def generate_credentials() ->dict:
    return{
           "username": "admin",
        "password": "password123"
    }