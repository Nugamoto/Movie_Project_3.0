"""
Module for fetching movie data from the OMDb API.

This module loads the OMDb API key from a .env file and defines a function
to fetch movie information (title, year, rating, actors, poster, etc.) using
the movie title as a search parameter.
"""

import os

import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment
API_KEY = os.getenv("OMDB_API_KEY")


def fetch_movie_data(title):
    """
    Fetch movie information from the OMDb API based on the movie title.

    Sends a GET request to the OMDb API and returns a dictionary containing
    movie details such as title, year, rating, actors, poster URL, etc.

    Handles cases where the movie is not found or the API is unreachable.

    :param title: The movie title to search for (string)
    :return: A dictionary with movie data if found, otherwise None
    """
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={title}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get("Response") == "True":
                return data
            else:
                print(f"\nMovie '{title}' not found")
                return None
        else:
            print("\nError fetching data!")
            return None
    except requests.exceptions.RequestException as e:
        print(f"\nAPI request failed: {e}")
        return None


if __name__ == "__main__":
    movie_title = "Titanic"
    result = fetch_movie_data(movie_title)
    if result:
        print(f"Title: {result.get('Title', '')}")
        print(f"Year: {result.get('Year', '')}")
        print(f"Rating: {result.get('imdbRating', '')}")
        print(f"Actors: {result.get('Actors', '')}")
