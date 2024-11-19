import tkinter as tk
from data_api import return_weather_data
from direct_api import get_suggestion

def get_id(city, window):
    #få dictionary av forslag fra API

    #sender navn, får to koordinater

    suggestions = get_suggestion(city)

    selected_id = tk.StringVar()

    suggestion_frame = tk.Frame(window, background='lightgray', padx=10, pady=10)
    suggestion_question = tk.Label(suggestion_frame,
                                   text='Velg riktig by',
                                   font='Times 24 bold',
                                   background='lightgray',
                                   pady=20)
    suggestion_question.pack()

    #lager selve knappene
    for elm in suggestions:
        suggestion = tk.Button(suggestion_frame,
                               text=elm['place'],
                               width=20,
                               padx=10,
                               pady=10,
                               command = lambda x=elm['coordinates']: (selected_id.set(x), suggestion_frame.destroy()) #lagrer riktig id
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