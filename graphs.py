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

def create_and_return_graphs(main_id, comparison_id=None):
    """
    Oppretter og returnerer fire vær-relaterte grafer med data fra en eller to steder.

    Parametere:
    - main_id (tuple): Koordinater for den første byen.
    - comparison_id (tuple, valgfri): Koordinater for den andre byen hvis sammenlikning ønskes.

    Returnerer:
    - Liste av matplotlib-figurobjekter.
    """
    lat1, lon1 = main_id
    # Hent værdata for første by
    weather_data1 = return_city_weather_data(lat1, lon1)
    time = format_time_labels(weather_data1['time'])

    # Sjekk om vi har en annen by for sammenlikning
    if comparison_id:
        lat2, lon2 = comparison_id
        weather_data2 = return_city_weather_data(lat2, lon2)

    # Opprett figurer
    figures = []

    # Temperatur og følt temperatur graf
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    ax1.plot(time, weather_data1['temperature'], marker='o', markersize=4, color='r', linestyle='-', label="Temperature (City 1)")
    ax1.plot(time, weather_data1['feels_like'], marker='o', markersize=4, color='r', linestyle='--', label="Feels Like (City 1)", alpha=0.7)
    
    if comparison_id:
        ax1.plot(time, weather_data2['temperature'], marker='o', markersize=4, color='b', linestyle='-', label="Temperature (City 2)")
        ax1.plot(time, weather_data2['feels_like'], marker='o', markersize=4, color='b', linestyle='--', label="Feels Like (City 2)", alpha=0.7)

    ax1.set_title("Temperature Over Time")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Temperature (°C)")
    ax1.tick_params(axis='x', rotation=-45)
    ax1.set_xticks(time[::3])  
    ax1.set_xticklabels(time[::3], ha='left') 
    ax1.legend()
    plt.tight_layout()
    figures.append(fig1)

    # Fuktighet graf
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    ax2.plot(time, weather_data1['humidity'], marker='o', markersize=4, color='b', linestyle='-', label="Humidity (City 1)")

    if comparison_id:
        ax2.plot(time, weather_data2['humidity'], marker='o', markersize=4, color='cyan', linestyle='-', label="Humidity (City 2)")

    ax2.set_title("Humidity Over Time")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Humidity (%)")
    ax2.tick_params(axis='x', rotation=-45)
    ax2.set_xticks(time[::3])  
    ax2.set_xticklabels(time[::3], ha='left')  
    ax2.legend()
    plt.tight_layout()
    figures.append(fig2)

    # Vindhastighet graf
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    ax3.plot(time, weather_data1['wind_speed'], marker='o', markersize=4, color='g', linestyle='-', label="Wind Speed (City 1)")

    if comparison_id:
        ax3.plot(time, weather_data2['wind_speed'], marker='o', markersize=4, color='lime', linestyle='-', label="Wind Speed (City 2)")

    ax3.set_title("Wind Speed Over Time")
    ax3.set_xlabel("Time")
    ax3.set_ylabel("Wind Speed (m/s)")
    ax3.tick_params(axis='x', rotation=-45)
    ax3.set_xticks(time[::3])  
    ax3.set_xticklabels(time[::3], ha='left')  
    ax3.legend()
    plt.tight_layout()
    figures.append(fig3)

    # Skydekke graf
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    ax4.plot(time, weather_data1['clouds'], marker='o', markersize=4, color='purple', linestyle='-', label="Cloud Coverage (City 1)")

    if comparison_id:
        ax4.plot(time, weather_data2['clouds'], marker='o', markersize=4, color='magenta', linestyle='-', label="Cloud Coverage (City 2)")

    ax4.set_title("Cloud Coverage Over Time")
    ax4.set_xlabel("Time")
    ax4.set_ylabel("Cloud Coverage (%)")
    ax4.tick_params(axis='x', rotation=-45)
    ax4.set_xticks(time[::3])  
    ax4.set_xticklabels(time[::3], ha='left') 
    ax4.legend()
    plt.tight_layout()
    figures.append(fig4)

    return figures

# Test case 
if __name__ == "__main__":
    
    main_id = (59.91, 10.75)  
    comparison_id = (57.90, 11.22)  

    # Kaller graf-funksjonen
    graphs = create_and_return_graphs(main_id, comparison_id)

    # Viser hver graf i hvert sitt vindu
    for fig in graphs:
        fig.show()  

    plt.show()
