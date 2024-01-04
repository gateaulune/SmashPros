import requests
import json

def get_current():
    username = input("Enter username: ")
    url = f"https://smashpros.gg/api/users/{username}" 
    headers = {'connect.sid':'s%3AAv83d7OKlLnLtL5sCr3dMn_tBjZfnMo8.Tirjake4GcvxCJI%2BZerNU%2Bx%2FQZJuVeHD8NiaEvfLleg'}  # Replace with your specific cookie value
    response = requests.get(url, headers=headers)

    # Check the response status code or any other conditions
    if response.status_code == 200:
        print('Request successful!')
        data = response.json()
        print(data)
    else:
        print(f"{response.status_code} | {response.reason}")
get_current()