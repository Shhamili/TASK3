from data_processor import load_movies, extend_movies_with_api_data, top_10_movies
from exporter import export_to_xml

def main():
    api_key = "b0f4f3f8"
    input_csv = 'movies.csv'
    output_xml = 'movies_extended.xml'

    # Încarcă datele inițiale
    df = load_movies(input_csv)

    # Extinde datele cu informații de pe OMDb
    df_extended = extend_movies_with_api_data(df, api_key)

    # Exportă datele extinse în XML
    export_to_xml(df_extended, output_xml)

    # Afișează top 10 filme
    top10 = top_10_movies(df_extended)
    print(top10[['title', 'imdb_rating']])

if __name__ == "__main__":
    main()
