from urllib import request
import requests
import pprint
import tkinter as tk
from tkinter import StringVar, messagebox
from tkinter import ttk




class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")
        self.geometry("400x400")
        self.configure(bg="#e0f7fa")
        self.city = ""
        # Location Entry
        self.location_label = ttk.Label(self, text="Enter Location:")
        self.location_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.city_var = tk.StringVar()
        self.location_entry = ttk.Entry(self, width=30, textvariable=self.city_var)
        self.location_entry.grid(row=0, column=1, padx=10, pady=10, sticky="we")

        self.search_button = ttk.Button(self, text="Get Weather")
        self.search_button.grid(row=0, column=2, padx=10, pady=10)
        self.search_button.bind('<Button-1>', self.click_get_city)
        # Weather Display Frame
        self.weather_frame = ttk.LabelFrame(self, text="Current Weather")
        self.weather_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        self.weather_icon = ttk.Label(self.weather_frame, text="Weather")
        self.weather_icon.grid(row=0, column=0, padx=10, pady=10)

        self.weather_info = ttk.Label(self.weather_frame, text="Temp: --\nCondition: --")
        self.weather_info.grid(row=0, column=1, padx=10, pady=10)

        # Forecast Frame
        self.forecast_frame = ttk.LabelFrame(self, text="Forecast")
        self.forecast_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Example forecast labels (you'd loop through actual data here)
        for i in range(5):
            day_label = ttk.Label(self.forecast_frame, text=f"Day {i+1}: --")
            day_label.grid(row=0, column=i, padx=5, pady=5)

        # Make columns expand nicely
        self.columnconfigure(1, weight=1)

    def click_get_city(self, event):
        self.city = self.city_var.get().strip()
        appid="6620adbdca1f561b30ab5e6c8c754a78" # use a openweathermap key here
        URL = "http://api.openweathermap.org/data/2.5/forecast"
        PARAMS = {"q": self.city, "appid": appid, "units": "metric", "lang": "RO"}
        try:
            response = requests.get(url=URL, params=PARAMS)   
            print(response.status_code)
            #On successful response, we'll get a status code of 200, so comparing
            # if the request was successful. 
            if response.status_code == 200:
                messagebox.showwarning("Saved", "Request was Successful") 
                data = response.json()
                self.city_var = ""
                pprint.pprint(data)
                self.weather_info.config(text=f"Temp: {data['list'][0]['main']['temp']}\nCondition: {data['list'][0]['weather'][0]['description']}")
                
            else:
                messagebox.showwarning("Selection Error", "Request was not Successful")
    #Handling any exceptions that may occur
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            messagebox.showwarning("Selection Error", f"Error: {e}")
        
    

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
