# Weather Data API

A Flask REST API serving historical daily mean temperatures from the European Climate Assessment & Dataset (ECA&D).

| Endpoint | Returns |
|---|---|
| `/` | Home page with the list of station IDs |
| `/api/v1/<station>/<date>` | Temperature for one station on one date, e.g. `/api/v1/10/1988-10-25` |
| `/api/v1/yearly/<station>/<year>` | All readings for one station in one year |
| `/api/v1/<station>` | All readings for one station |

## Data

The dataset is not included because of its size. Download the *blended daily mean temperature (TG)* ASCII files from [ECA&D](https://www.ecad.eu/dailydata/predefinedseries.php) and put `stations.txt` and the `TG_STAID*.txt` files in `data_small/`.

## Run

```bash
pip install -r requirements.txt
python main.py
```
