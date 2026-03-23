# Weather App

A simple weather app made with Python. It shows current weather of any city.
It has two versions - one runs in the terminal and one has a GUI window.

---

## What it shows

- Temperature (in Celsius)
- Weather condition
- Humidity
- Wind Speed

---

## Requirements

- Python 3
- requests library

Install requests by running this in terminal:
```
pip install requests
```

---

## How to run

Just run the file:
```
python weather_app.py
```

This will open the GUI window.

If you want to use the console version instead, call the function manually at the bottom of the file:
```python
run_console()
```

---

## API Key

This app uses OpenWeatherMap to get weather data.
The API key is already in the code so it should work out of the box.

If it stops working you can get a free API key from:
https://openweathermap.org/api

Then replace this line in the code:
```python
API_KEY = "your_api_key_here"
```

---

## Files

```
weather_app.py    # main file, has both console and GUI version
README.md         # this file
```
