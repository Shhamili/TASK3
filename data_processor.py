import pandas as pd
from api_client import get_movie_data

def load_movies(filepath):
    return pd.read_csv(filepath)

def extend_movies_with_api_data(df, api_key):
    ratings = []
    actors = []
    votes = []

    for _, row in df.iterrows():
        title = row['title']
        year = row['release_year']
        print(f"[INFO] Preluare date pentru: {title} ({year})")
        movie_data = get_movie_data(title, year, api_key)
        print(f"[DEBUG] Răspuns API: {movie_data}")
        

        ratings.append(movie_data['imdb_rating'])
        actors.append(movie_data['actors'])
        votes.append(movie_data['imdb_votes'])

    df['imdb_rating'] = ratings
    df['actors'] = actors
    df['imdb_votes'] = votes

    return df

def top_10_movies(df):
    df['imdb_rating'] = pd.to_numeric(df['imdb_rating'], errors='coerce')
    return df.sort_values('imdb_rating', ascending=False).head(10)
