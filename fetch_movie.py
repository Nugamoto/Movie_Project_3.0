import requests
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key from environment
API_KEY = os.getenv("OMDB_API_KEY")


def fetch_movie_data(title):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={title}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            return data
        else:
            print("Movie not found!")
            return None
    else:
        print("Error fetching data!")
        return None


# Test
if __name__ == "__main__":
    movie_title = "Titanic"
    result = fetch_movie_data(movie_title)
    if result:
        print(f"Title: {result['Title']}")
        print(f"Year: {result['Year']}")
        print(f"Rating: {result['imdbRating']}")
        print(f"Actors: {result['Actors']}")