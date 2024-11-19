import tkinter as tk
from tkinter_functions import get_id, info_box

window = tk.Tk()
window.title('Å være eller ikke være')

window_width = 1000
window_height = 650

#deklarerer globale id-variabler
main_id = []
comparison_id = []

#container til input for å midtstille
input_container = tk.Frame(window)

#main city widget
main_city_input = tk.StringVar()
main_city_widget = tk.Entry(input_container, 
                            borderwidth=10, 
                            relief=tk.FLAT,
                            textvariable=main_city_input)
main_city_widget.insert(index=0, string='Hovedby')
main_city_widget.pack(side="left")

#comparison city widget
comparison_city_input = tk.StringVar()
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
    global main_id
    global comparison_id
    main_id = get_id(main_city_input.get(), window)
    comparison_id = get_id(comparison_city_input.get(), window)
    print(main_id, comparison_id)

#enter knapp
enter_btn = tk.Button(input_container,
                      text='Enter',
                      command=enter_btn_func)
enter_btn.pack(side="left")
input_container.pack(side="left", anchor='nw', padx=10, pady=10)

window.geometry(f"{window_width}x{window_height}")

#kjører vinduet

#info_box(main_id[0], main_id[1], window)

window.mainloop()