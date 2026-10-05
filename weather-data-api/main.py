import os
from flask import Flask, render_template
import pandas as pd

DATA_DIR = "data_small"

app = Flask(__name__)


def station_file(station):
    return os.path.join(DATA_DIR, "TG_STAID" + str(station).zfill(6) + ".txt")


@app.route("/")
def home():
    stations = pd.read_csv(os.path.join(DATA_DIR, "stations.txt"), skiprows=17)
    stations.columns = stations.columns.str.strip()
    stations = stations[["STAID", "STANAME"]]
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def api(station, date):
    df = pd.read_csv(station_file(station), skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {"station": station, "date": date, "temperature": temperature}


@app.route("/api/v1/yearly/<station>/<year>")
def yearly_data(station, year):
    df = pd.read_csv(station_file(station), skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result


@app.route("/api/v1/<station>")
def all_data(station):
    df = pd.read_csv(station_file(station), skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")
    return result


if __name__ == "__main__":
    app.run(debug=True)
