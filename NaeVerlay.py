import tkinter as tk
from tkinter import *
import time
import requests
import json


#   TKINTER INTERFACE SETTINGS
root = tk.Tk()
root.title("SmashPros Tracker")
root.geometry("250x150")    
font_size = 14
dylan_size = 12
credit_size = 8
total_size = 12
#   API REQUESTS
url = f"https://smashpros.gg/api/users/naetoru"
headers = {'connect.sid':'s%3AAv83d7OKlLnLtL5sCr3dMn_tBjZfnMo8.Tirjake4GcvxCJI%2BZerNU%2Bx%2FQZJuVeHD8NiaEvfLleg'}  # Replace with your specific cookie value
response = requests.get(url, headers=headers)

#   API REQUESTS CHECK
def api_request():
    if response.status_code == 200:
        print('Request successful!')
        data = response.json()
        id = data['id']
        rating = data['skillRating']['rating']
        url_ratio = f"https://smashpros.gg/api/users/{id}/wins-losses"
        response_ratio = requests.get(url_ratio, headers=headers)
        data_ratio = response_ratio.json()
        wins_ratio = data_ratio['wins']
        losses_ratio = data_ratio['losses']
        return wins_ratio, losses_ratio, rating
    else:
        print(f"{response.status_code} | {response.reason}")
# API OUTPUT


wins_ratio, losses_ratio, rating = api_request()
#   TKINTER INTERFACE


user_label = tk.Label(root, text=f"NaetorU 's Stats", font=("Arial", dylan_size))
user_label.pack(anchor='n')

elo_label = tk.Label(root, text=f"ELO : {rating}", font=("Arial", font_size))
elo_label.pack(anchor='w')   
win_label = tk.Label(root, text=f"Wins : {wins_ratio}", font=("Arial", font_size))
win_label.pack(anchor='w')    
losses_label = tk.Label(root, text=f"Losses : {losses_ratio}",font=("Arial", font_size))
losses_label.pack(anchor='w')
total_label = tk.Label(root, text=f"Total : {wins_ratio + losses_ratio}",font=("Arial", total_size))
total_label.pack(anchor='nw')
credit_label = tk.Label(root, text=f"Made by @Its_Charlottees",font=("Arial", credit_size))
credit_label.pack(anchor='ne')

def update_labels():
    wins_ratio, losses_ratio, rating = api_request()
    elo_label.config(text=f"ELO : {rating}")    
    win_label.config(text=f"Wins : {wins_ratio}")
    losses_label.config(text=f"Losses : {losses_ratio}")
    root.after(60000, update_labels)  # Schedule this function to be called again after 60000 milliseconds (1 minute)

# Call the function once to start the updates
update_labels()

root.mainloop()