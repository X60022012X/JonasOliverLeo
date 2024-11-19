import tkinter as tk
from data_api import return_weather_data

def get_id(city, window):
    #få dictionary av forslag fra API

    #sender navn, får to koordinater

    example_suggestions_main = [
        {"name": "Oslo, NO", "id": 12345},
        {"name": "Berlin, DE", "id": 67890},
        {"name": "Paris, FR", "id": 54321},
        {"name": "Tokyo, JP", "id": 98765},
        {"name": "New York, US", "id": 45678},
        {"name": "Sydney, AU", "id": 19283}
    ] #skal byttes ut med liste over mulige steder, returnert fra api

    selected_id = tk.IntVar()

    suggestion_frame = tk.Frame(window, background='lightgray', padx=10, pady=10)
    suggestion_question = tk.Label(suggestion_frame,
                                   text='Velg riktig by',
                                   font='Times 24 bold',
                                   background='lightgray',
                                   pady=20)
    suggestion_question.pack()

    #lager selve knappene
    for elm in example_suggestions_main:
        suggestion = tk.Button(suggestion_frame,
                               text=elm['name'],
                               width=20,
                               padx=10,
                               pady=10,
                               command = lambda x=elm['id']: (selected_id.set(x), suggestion_frame.destroy()) #lagrer riktig id
        )
        suggestion.pack()

    suggestion_frame.pack()
    suggestion_frame.place(x=window.winfo_width()/2, y=window.winfo_height()/2-200, anchor='n')

    window.wait_variable(selected_id)
    return selected_id.get()

def info_box(lan, lon, window):
    info_frame = tk.Frame(window)

    weather_data = return_weather_data(lan, lon)
    weather_info = weather_data["weather_info"]

    print(weather_info)

    info_frame.pack(side="right", anchor='ne')