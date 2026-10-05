# Movie Recommender

Three approaches to movie recommendation, one notebook each:

| Notebook | Approach |
|---|---|
| `popularity_based_recommendation.ipynb` | Ranks movies by the IMDB weighted rating, `WR = v/(v+m)·R + m/(v+m)·C` |
| `content_based_recommendation.ipynb` | TF-IDF vectors of plot overviews and cosine similarity to find similar movies |
| `rating_prediction_svd.ipynb` | Collaborative filtering with SVD (Surprise), evaluated with 5-fold cross-validated RMSE and MAE |

## Data

`movies_small.csv` is included. The larger files are not:

- `movies.csv` and `credits.csv`: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) on Kaggle
- `ratings.csv`: [MovieLens latest small](https://grouplens.org/datasets/movielens/latest/)

## Run

```bash
pip install -r requirements.txt
jupyter notebook
```
