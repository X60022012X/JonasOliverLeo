import tkinter as tk
from data_api import return_city_info, return_city_weather_data
from direct_api import get_suggestion
import ast
from math import floor

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
    for key, value in suggestions.items():
        suggestion = tk.Button(suggestion_frame,
                               text=key,
                               width=20,
                               padx=10,
                               pady=10,
                               command = lambda x=value: (selected_id.set(x),
                                                          suggestion_frame.destroy()) #lagrer riktig id
        )
        suggestion.pack()

    suggestion_frame.pack()
    suggestion_frame.place(x=window.winfo_width()/2, y=window.winfo_height()/2-200, anchor='n')

    window.wait_variable(selected_id)
    selected_id_tuple = ast.literal_eval(selected_id.get())
    #print(selected_id_tuple)
    return selected_id_tuple

info_font_size = 1

def info_box(main_coordinates, comparison_coordinates, window):

    # Create the frame to hold the information
    info_frame = tk.Frame(window, bg='lightgray')
    
    # Fetch weather data (assuming return_weather_data is defined elsewhere)
    main_weather_info = return_city_info(main_coordinates[0], main_coordinates[1])
    comparison_weather_info = return_city_info(comparison_coordinates[0], comparison_coordinates[1])
    print('main:', main_weather_info)
    print('comparison:', comparison_weather_info)

    # Data (Rows for Population, Land, Timezone)
    data = [
        ("Population:", main_weather_info['population'], comparison_weather_info['population']),
        ("Land:", main_weather_info['country'], comparison_weather_info['country']),
        ("Timezone:", main_weather_info['timezone'], comparison_weather_info['timezone']['UTC'])
    ]

    # Configure grid layout for uniform spacing
    for i in range(len(data)):
        info_frame.columnconfigure(i, weight=1)
    for i in range(4):  # Adjust for rows (including headers and data rows)
        info_frame.rowconfigure(i, weight=1)
    
    # Header (Information)
    info_title = tk.Label(info_frame, 
                          text='Informasjon', 
                          font=f'Arial {floor(20*info_font_size)} bold', 
                          bg='lightgray', 
                          anchor="center")
    info_title.grid(row=0, column=0, columnspan=3, sticky="nsew", pady=10)
    
    # Subheadings (Column titles)
    columns = ["", main_weather_info['name'], comparison_weather_info['name']]
    for col, text in enumerate(columns):
        column_label = tk.Label(info_frame, 
                                text=text, 
                                font=f'Arial {floor(12*info_font_size)} bold', 
                                bg='lightgray', 
                                anchor="center")
        column_label.grid(row=1, column=col, sticky="nsew", padx=5, pady=5)
    
    
    for row_idx, row_data in enumerate(data, start=2):
        for col_idx, cell_data in enumerate(row_data):
            data_label = tk.Label(info_frame, 
                                  text=cell_data, 
                                  font=f'Arial {floor(12*info_font_size)}', 
                                  bg='lightgray', 
                                  anchor="center")
            data_label.grid(row=row_idx, column=col_idx, sticky="nsew", padx=5, pady=5)
    
    # Pack the frame to the right of the window
    info_frame.pack(side="right", anchor='ne', expand=True, padx=90, pady=10)