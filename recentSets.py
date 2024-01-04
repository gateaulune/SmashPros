import requests

def get_current():
    url = 'https://smashpros.gg/api/sets/recent'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print('Bad request - Please check the error code')
        print(f"{requests.status_codes} | {requests.reason}" )
get_current()