import tkinter as tk
from tkinter_functions import get_id, info_box, figure_frame
from graphs import create_and_return_graphs

window = tk.Tk()
window.title('Å være eller ikke være')

window_width = 1000
window_height = 650

#deklarerer globale id-variabler
main_id = []
comparison_id = []

#refresh vindu funksjon
def refresh_window():
    global main_id, comparison_id
    for child in window.winfo_children()[2:]: #sletter alle elementer bortsett fra refresh-knapp og input
        child.destroy()
    main_id = comparison_id
    comparison_id = [] #nullstiller variabler

#refresj-knapp
refresh_btn = tk.Button(window,
                        text='Refresh',
                        command=refresh_window)
refresh_btn.pack()

#container til input for å midtstille
input_container = tk.Frame(window)

#main city widget
main_city_input = tk.StringVar() #variabel for å hente input
main_city_widget = tk.Entry(input_container, 
                            borderwidth=10, 
                            relief=tk.FLAT,
                            textvariable=main_city_input)
main_city_widget.insert(index=0, string='Hovedby')
main_city_widget.pack(side="left")

#comparison city widget
comparison_city_input = tk.StringVar() #variabel for å hente input
comparison_city_wigdet = tk.Entry(input_container,
                                  borderwidth=10,
                                  relief=tk.FLAT,
                                  textvariable=comparison_city_input)
comparison_city_wigdet.insert(index=0, string='By å sammenlikne med')
comparison_city_wigdet.pack(side="left")


#funksjon til å slette placeholder ved trykk
def erase_placeholder(event):
    event.widget.delete(0, "end")

main_city_widget.bind("<Button-1>", erase_placeholder)
comparison_city_wigdet.bind("<Button-1>", erase_placeholder)

#enter knapp funksjon
def enter_btn_func():
    refresh_window()

    global main_id, comparison_id

    main_id = get_id(main_city_input.get(), window) 
    
    # Hent ID for sammenligningsby hvis input ikke er tom
    if comparison_city_input.get() not in {'', ' ', '   '}:
        comparison_id = get_id(comparison_city_input.get(), window)

    # Slett eksisterende info-boks før ny blir laget
    for child in window.winfo_children():
        if isinstance(child, tk.Frame) and child.cget('bg') == 'lightgray':  # Identifiser info-boks basert på bakgrunnsfarge
            child.destroy()

    # Opprett ny info-boks med oppdaterte ID-er
    info_box(window, main_id, comparison_id)  

    # Hent grafene til byene, navn og ID er parametere
    figures = create_and_return_graphs(main_city_input.get(), comparison_city_input.get(), main_id, comparison_id)


    figure_frame(figures, window)


#enter knapp
enter_btn = tk.Button(input_container,
                      text='Enter',
                      command=enter_btn_func)
enter_btn.pack(side="left") #legger til knappen
input_container.pack(side="left", anchor='nw', padx=10, pady=10)

window.geometry(f"{window_width}x{window_height}") #bestemmer størrelse på vinduet

#kjører vinduet
window.mainloop()