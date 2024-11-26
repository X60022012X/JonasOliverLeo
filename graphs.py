import matplotlib.pyplot as plt
from datetime import datetime
from data_api import return_city_weather_data

def format_time_labels(time_data):
    """
    Formaterer tid slik: "dag/måned/år time".
    """
    formatted_times = []
    for time in time_data:
        dt_object = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        formatted_time = dt_object.strftime('%d/%m/%y %H')
        formatted_times.append(formatted_time)
    return formatted_times

def create_and_return_graphs(main_name, comparison_name, main_id, comparison_id=None):

    figsize = (7, 5)
    dpi = 90
    """
    Oppretter og returnerer fire vær-relaterte grafer med data fra en eller to steder.

    Parametere:
    - main_id (tuple): Koordinater for den første byen.
    - comparison_id (tuple, valgfri): Koordinater for den andre byen hvis sammenlikning ønskes.

    Returnerer:
    - Liste av matplotlib-figurobjekter.
    """
    
    # Hent værdata for første by
    weather_data1 = return_city_weather_data(main_id)
    time = format_time_labels(weather_data1['time'])

    # Sjekk om vi har en annen by for sammenlikning
    if comparison_id:
        weather_data2 = return_city_weather_data(comparison_id)

    # Opprett figurer
    figures = []

    # Temperatur og følt temperatur graf
    fig1, ax1 = plt.subplots(figsize=figsize, dpi = dpi)
    ax1.plot(time, weather_data1['temperature'], marker='o', markersize=4, color='r', linestyle='-', label=f"Temperatur, {main_name}")
    ax1.plot(time, weather_data1['feels_like'], marker='o', markersize=4, color='r', linestyle='--', label=f"Føles som, {main_name}", alpha=0.7)
    
    if comparison_id:
        ax1.plot(time, weather_data2['temperature'], marker='o', markersize=4, color='b', linestyle='-', label=f"Temperatur, {comparison_name}")
        ax1.plot(time, weather_data2['feels_like'], marker='o', markersize=4, color='b', linestyle='--', label=f"Føles som, {comparison_name}", alpha=0.7)

    ax1.set_title("Temperatur over tid")
    ax1.set_xlabel("Tid")
    ax1.set_ylabel("Temperatur (°C)")
    ax1.tick_params(axis='x', rotation=-45)
    ax1.set_xticks(time[::3])  
    ax1.set_xticklabels(time[::3], ha='left') 
    ax1.legend()
    plt.tight_layout()
    figures.append(fig1)

    # Fuktighet graf
    fig2, ax2 = plt.subplots(figsize=figsize, dpi = dpi)
    ax2.plot(time, weather_data1['humidity'], marker='o', markersize=4, color='b', linestyle='-', label=f"Luftfuktighet, {main_name}")

    if comparison_id:
        ax2.plot(time, weather_data2['humidity'], marker='o', markersize=4, color='cyan', linestyle='-', label=f"Luftfuktighet, {comparison_name}")

    ax2.set_title("Fuktighet over tid")
    ax2.set_xlabel("Tid")
    ax2.set_ylabel("Fuktighet (%)")
    ax2.tick_params(axis='x', rotation=-45)
    ax2.set_xticks(time[::3])  
    ax2.set_xticklabels(time[::3], ha='left')  
    ax2.legend()
    plt.tight_layout()
    figures.append(fig2)

    # Vindhastighet graf
    fig3, ax3 = plt.subplots(figsize=figsize, dpi = dpi)
    ax3.plot(time, weather_data1['wind_speed'], marker='o', markersize=4, color='g', linestyle='-', label=f"Vind, {main_name}")

    if comparison_id:
        ax3.plot(time, weather_data2['wind_speed'], marker='o', markersize=4, color='lime', linestyle='-', label=f"Vind, {comparison_name}")

    ax3.set_title("Vind over tid")
    ax3.set_xlabel("Tid")
    ax3.set_ylabel("Vind (m/s)")
    ax3.tick_params(axis='x', rotation=-45)
    ax3.set_xticks(time[::3])  
    ax3.set_xticklabels(time[::3], ha='left')  
    ax3.legend()
    plt.tight_layout()
    figures.append(fig3)

    # Skydekke graf
    fig4, ax4 = plt.subplots(figsize=figsize, dpi = dpi)
    ax4.plot(time, weather_data1['clouds'], marker='o', markersize=4, color='purple', linestyle='-', label=f"Skydekke, {main_name}")

    if comparison_id:
        ax4.plot(time, weather_data2['clouds'], marker='o', markersize=4, color='magenta', linestyle='-', label=f"Skydekke, {comparison_name}")

    ax4.set_title("Skydekke over tid")
    ax4.set_xlabel("Tid")
    ax4.set_ylabel("Skydekke (%)")
    ax4.tick_params(axis='x', rotation=-45)
    ax4.set_xticks(time[::3])  
    ax4.set_xticklabels(time[::3], ha='left') 
    ax4.legend()
    plt.tight_layout()
    figures.append(fig4)

    return figures

# Test case 
if __name__ == "__main__":
    
    main_id = 'London, England, GB'
    comparison_id = 'Houston, Texas, US'

    # Kaller graf-funksjonen
    graphs = create_and_return_graphs('London', 'Houston', main_id, comparison_id)

    # Viser hver graf i hvert sitt vindu
    for fig in graphs:
        fig.show()  

    plt.show()
