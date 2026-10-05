import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_data(place, days):
    """Return the 3-hourly forecast entries for the next `days` days."""
    if not API_KEY:
        raise RuntimeError("Set OPENWEATHER_API_KEY (get a free key at https://openweathermap.org/api)")
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {"q": place, "appid": API_KEY, "units": "metric"}
    response = requests.get(url, params=params)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * days
    return filtered_data[:nr_values]


if __name__ == "__main__":
    print(get_data(place="London", days=3))
