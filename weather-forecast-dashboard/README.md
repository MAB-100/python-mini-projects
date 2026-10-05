# Weather Forecast Dashboard

A Streamlit dashboard for the forecast of up to five days in any city, using the [OpenWeather](https://openweathermap.org/api) 5-day forecast API.

- **Temperature:** interactive Plotly line chart (°C)
- **Sky:** one icon per 3-hour slot (clear, clouds, rain, snow)

## Run

```bash
pip install -r requirements.txt
export OPENWEATHER_API_KEY=your-openweather-key
streamlit run main.py
```
