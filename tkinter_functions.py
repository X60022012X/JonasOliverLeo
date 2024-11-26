import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import ast
from math import floor
from data_api import return_city_info
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
    for key in suggestions.keys():
        suggestion = tk.Button(suggestion_frame,
                               text=key,
                               width=20,
                               padx=10,
                               pady=10,
                               command = lambda x=key: (selected_id.set(x), #lagrer riktig id
                                                          suggestion_frame.destroy()) #sletter forslag
        )
        suggestion.pack()

    suggestion_frame.pack()
    suggestion_frame.place(x=window.winfo_width()/2, y=window.winfo_height()/2-200, anchor='n')

    window.wait_variable(selected_id)
    #selected_id_tuple = ast.literal_eval(selected_id.get())
    return selected_id.get()

info_font_size = 1

def info_box(window, main_city, comparison_city=None):

    # lager info frame
    info_frame = tk.Frame(window, bg='lightgray')
    
    # henter værdata
    main_weather_info = return_city_info(main_city)
    if comparison_city:
        comparison_weather_info = return_city_info(comparison_city)

    # Data (Rader for populasjon, land, tidssone)
    if comparison_city:
        data = [
            ("Befolkning:", main_weather_info['population'], comparison_weather_info['population']),
            ("Land:", main_weather_info['country'], comparison_weather_info['country']),
            ("Tidssone:", main_weather_info['timezone']['UTC'], comparison_weather_info['timezone']['UTC'])
        ]
    else:
        data = [
            ("Befolkning:", main_weather_info['population']),
            ("Land:", main_weather_info['country']),
            ("Tidssone:", main_weather_info['timezone']['UTC'])
        ]

    # lager grid layout for strukturert oversikt
    for i in range(len(data)):
        info_frame.columnconfigure(i, weight=1)
    for i in range(4):  # kan tilpasses for antall rader
        info_frame.rowconfigure(i, weight=1)
    
    # Lager overskrit
    info_title = tk.Label(info_frame, 
                          text='Informasjon', 
                          font=f'Arial {floor(20*info_font_size)} bold', 
                          bg='lightgray', 
                          anchor="center")
    info_title.grid(row=0, column=0, columnspan=3, sticky="nsew", pady=10)
    
    # Lager kolonne titler
    if comparison_city:
        columns = ["", main_weather_info['name'], comparison_weather_info['name']]
    else:
         columns = ["", main_weather_info['name']]


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
    
    # Legger til info frame i hoved-vinduet
    info_frame.pack(side="right", anchor='ne', expand=True, padx=90, pady=10)





def figure_frame(figures, window):
    current_index = 0
    #bytter index for figurer
    def next_index():
        nonlocal current_index
        current_index = (current_index + 1) % len(figures)

    def prev_index():
        nonlocal current_index
        current_index = (current_index - 1) % len(figures)

    #lager frame for grafer
    graph_frame = tk.Frame(window, width=800, height=600, bg='black')  # lengde og bredde kan variere
    graph_frame.pack()
    graph_frame.place(x=5, y=130)

    canvas_frame = tk.Frame(graph_frame)
    canvas_frame.pack(side='bottom', fill='both', expand=True)

    #tegner grafen
    def draw_graph(figure, canvas_frame):
        for child in canvas_frame.winfo_children():
            child.destroy()

        canvas = FigureCanvasTkAgg(figure, master=canvas_frame)

        canvas.draw()
        canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2Tk(canvas)

        toolbar.update()
        toolbar.pack(side='bottom', fill='x')

        canvas.get_tk_widget().pack(side='bottom', anchor='sw', fill='both', expand=True)

    

    next_graph_btn = tk.Button(graph_frame,
                               text='Neste',
                               command=lambda: (next_index(), draw_graph(figures[current_index], canvas_frame)))
    next_graph_btn.pack(side='right', padx=5, pady=5)
    
    prev_graph_btn = tk.Button(graph_frame,
                               text='Forrige',
                               command=lambda: (prev_index(), draw_graph(figures[current_index], canvas_frame)))
    prev_graph_btn.pack(side='left', padx=5, pady=5)

    graph_frame.config(height=200, width=300)
    draw_graph(figures[current_index], canvas_frame)