import tkinter as tk
from tkinter import ttk
import time
import requests
import json

def stats():
    # TKINTER INTERFACE SETTINGS
    root = tk.Tk()
    root.title("SmashPros Tracker")
    root.geometry("500x300")
    root.iconbitmap("./assets/images.ico")
    # Create a frame with a green background
    frame = tk.Frame(root, bg="#00FF00")
    frame.pack(fill=tk.BOTH, expand=True)

    font_size = 22
    dylan_size = 26
    total_size = 20

    # API REQUESTS
    url = f"https://smashpros.gg/api/users/naetoru"
    headers = {'connect.sid':'s%3AAv83d7OKlLnLtL5sCr3dMn_tBjZfnMo8.Tirjake4GcvxCJI%2BZerNU%2Bx%2FQZJuVeHD8NiaEvfLleg'}  # Cookie
    response = requests.get(url, headers=headers)

    # API REQUESTS CHECK

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

    # TKINTER INTERFACE
    user_label = tk.Label(frame, text=f"NaetorU 's Stats", font=("Arial", dylan_size), bg="#00FF00", fg="white")
    user_label.pack(anchor='nw')

    elo_label = tk.Label(frame, text=f"\nElo : {rating}", font=("Arial", font_size), bg="#00FF00", fg="white")
    elo_label.pack(anchor='w')

    win_label = tk.Label(frame, text=f"Wins : {wins_ratio}", font=("Arial", font_size), bg="#00FF00", fg="white")
    win_label.pack(anchor='w')

    losses_label = tk.Label(frame, text=f"Losses : {losses_ratio}", font=("Arial", font_size), bg="#00FF00",fg="white")
    losses_label.pack(anchor='w')

    total_label = tk.Label(frame, text=f"Total : {wins_ratio + losses_ratio}", font=("Arial", total_size), bg="#00FF00",fg="white")
    total_label.pack(anchor='nw')
    def update_labels():
        wins_ratio, losses_ratio, rating = api_request()
        print(wins_ratio, losses_ratio, rating )
        elo_label.config(text=f"Elo : {rating}")
        win_label.config(text=f"Wins : {wins_ratio}")
        losses_label.config(text=f"Losses : {losses_ratio}")
        total_label.config(text=f"Total : {wins_ratio + losses_ratio}")
        root.after(60000, update_labels)  # (1 minute)
    update_labels()
    root.mainloop()
stats()
