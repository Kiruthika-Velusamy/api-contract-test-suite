import requests

#Variables and types
base_url="https://www.google.com"
booking_id=43
is_paid=True
price = 12.30
print(f"Fetching booking id {booking_id} from {base_url}")
print(type(price))

#List
booking_id = [1,2,3,4,5]
print(booking_id[0])
print(booking_id[-1])
booking_id.append(6)
print(booking_id)
print(len(booking_id));

#For loop
for id in booking_id:
 print(f"booking id is {id}")

#While loop
count=0
while count<4:
 print(f"count is {count}")
 count+=1

#Range
for i in range(5):
 print(f"Range is {i}")

#Conditionals
code = 200
if code==200:
 print("Success")
elif code==404:
 print("Not found")
elif code==401:
 print("Unauthorised")
else:
 print(f"Unexpected status: {code}")

#Dictionaries
booking = {
    "firstname": "Jane",
    "lastname": "Doe",
    "totalprice": 150,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2026-01-01",
        "checkout": "2026-01-05"
    }
}

print(booking["firstname"])
print(booking["bookingdates"]["checkin"])
print(booking.get("lastname"))

booking["email"]="abc@gmail.com"

for key,value in booking.items():
 print(f"{key} : {value}")

if "firstname" in booking:
 print("firstname exists")

#Tuples
credentials =("admin", "password")
username=credentials[0]
password=credentials[1]
print(f"Username : {username}")
print(f"Username : {password}")


#List comprehensions
#Normal loop
prices =[10,20,30,40,50]
doubled =[]
for p in prices:
 doubled.append(2*p)
print(doubled)

#List comprehension(same in one line)
doubled =[p* 2 for p in prices]
print(doubled)

#With Condition
expensive =[p for p in prices if p>20]
print(expensive)

#Function with Type Hints
print("-----------Function with Type Hints--------------")
def greet(name:str)-> str:
 return f"Hello,{name}"

print(greet("Kiruthika"))


#Function with multiple parameters
print("-----------Function with Multiple parameters--------------")
def create_booking(firstname:str, lastname:str, price:int)->dict:
   return {
      "firstname":firstname,
      "lastname":lastname,
      "Price":price,
      "bookingdates": {
        "checkin": "2026-01-01",
        "checkout": "2026-01-05"
    }

   }
print(create_booking("Kiruthika","Velusamy",50))



#Exceptions
print("-----------Exceptions---------------")
def get_booking(booking_id:str) ->dict:
 try:
  response= requests.get (f"https://restful-booker.herokuapp.com/booking/{booking_id}")
  response.raise_for_status()
  return response.json()

 except requests.exceptions.ConnectionError:
    print("Cannot connect to Server")
    return{}
 except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
    return{}
 except requests.Exceptions as e:
    print(f"Unpexpected error: {e}")
    return{}

booking =get_booking(1)
print(booking)