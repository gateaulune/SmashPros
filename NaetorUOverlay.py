import tkinter as tk
from tkinter import *
import time
import requests
import json


def overlay():
    get_ratio()
    root = tk.Tk()
    root.geometry("250x100")
    url = f"https://smashpros.gg/api/users/naetoru"
    headers = {'connect.sid':'s%3AAv83d7OKlLnLtL5sCr3dMn_tBjZfnMo8.Tirjake4GcvxCJI%2BZerNU%2Bx%2FQZJuVeHD8NiaEvfLleg'}  # Replace with your specific cookie value
    response = requests.get(url, headers=headers)
    font_size = 24
    # Create the main window
    

    # Add a label
    label = tk.Label(root, text=f"{wins_ratio}", font=("Arial", font_size))
    label.pack()

    # Add a button
    button = tk.Label(root, text=f"{losses_ratio}",font=("Arial", font_size))
    button.pack()
    ratio_boucle()
    # Enter the main loop
    root.mainloop()


def get_ratio():
    url = f"https://smashpros.gg/api/users/naetoru"
    headers = {'connect.sid':'s%3AAv83d7OKlLnLtL5sCr3dMn_tBjZfnMo8.Tirjake4GcvxCJI%2BZerNU%2Bx%2FQZJuVeHD8NiaEvfLleg'}  # Replace with your specific cookie value
    response = requests.get(url, headers=headers)

    # Check the response status code or any other conditions
    if response.status_code == 200:
        print('Request successful!')
        data = response.json()
        id = data['id']
        url_ratio = f"https://smashpros.gg/api/users/{id}/wins-losses"
        response_ratio = requests.get(url_ratio, headers=headers)
        data_ratio = response_ratio.json()
        wins_ratio = data_ratio['wins']
        looses_ratio = data_ratio['losses']
    else:
        print(f"{response.status_code} | {response.reason}")
#get_ratio()

def ratio_boucle():
    while True:
        get_ratio()
        time.sleep(5)


overlay()







