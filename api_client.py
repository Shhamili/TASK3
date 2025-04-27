import requests
from urllib.parse import quote_plus

def get_movie_data(title, year, api_key):
    title_encoded = quote_plus(title)
    url = f"http://www.omdbapi.com/?t={title_encoded}&y={year}&apikey={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data.get('Response') == 'True':
            return {
                'imdb_rating': data.get('imdbRating', 'N/A'),
                'actors': data.get('Actors', 'N/A'),
                'imdb_votes': data.get('imdbVotes', 'N/A')
            }
    return {'imdb_rating': 'N/A', 'actors': 'N/A', 'imdb_votes': 'N/A'}
