import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "9dcfa0c2376c2fc47e8bd3536c8d13a1"

# console
def run_console():
    while True:
        city = input("Enter city name: ")

        if city == "":
            print("Please enter a city name")
            continue

        url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY + "&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                temp = data["main"]["temp"]
                condition = data["weather"][0]["description"]
                humidity = data["main"]["humidity"]
                wind = data["wind"]["speed"]

                print("\nWeather in " + city + ":")
                print("Temperature:", temp, "C")
                print("Condition:", condition)
                print("Humidity:", humidity, "%")
                print("Wind Speed:", wind, "m/s")
            else:
                print("Error:", data["message"])

        except:
            print("Something went wrong. Check your internet.")

        again = input("\nSearch another city? (yes/no): ")
        if again != "yes":
            print("Goodbye!")
            break


# gui version
def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return

    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY + "&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            condition = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]

            result = "Weather in " + city + "\n"
            result = result + "Temperature: " + str(temp) + " C\n"
            result = result + "Condition: " + condition + "\n"
            result = result + "Humidity: " + str(humidity) + "%\n"
            result = result + "Wind Speed: " + str(wind) + " m/s"

            result_label.config(text=result)

        else:
            result_label.config(text="Error: " + data["message"])

    except:
        result_label.config(text="Something went wrong. Check your internet.")


# main window
root = tk.Tk()
root.title("Weather App")
root.geometry("300x280")

tk.Label(root, text="Weather App", font=("Arial", 14)).pack(pady=10)

tk.Label(root, text="Enter City:").pack()
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", bg="blue", fg="white", command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)

root.mainloop()