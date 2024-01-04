import requests
import json






def get_current_set():
    url = 'https://smashpros.gg/api/sets/in-progress/count'
    headers = {
        "_ga": "GA1.1.1915540312.1703083565",
        "connect.sid": "s%3AAv83d7OKlLnLtL5sCr3dMn_tBjZfnMo8.Tirjake4GcvxCJI%2BZerNU%2Bx%2FQZJuVeHD8NiaEvfLleg",
        "_ga_W6ZL09PE1Y": "GS1.1.1703083564.1.1.1703084507.0.0.0",
        }  # Replace with your specific cookie value
    
    response = requests.get(url, headers=headers)

    # Check the response status code or any other conditions
    if response.status_code == 200:
        data = response.json()
        counting = data['count']
        print("Current number of sets in progress: " + str(counting))
    else:
        print(f"{response.status_code} | {response.reason}") 
        print(response.headers)
        print(headers)

get_current_set()

