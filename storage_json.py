import json
import os

from istorage import IStorage


class StorageJson(IStorage):
    """JSON-based implementation of the IStorage interface for managing movie data."""

    def __init__(self, file_path):
        """
        Initialize the StorageJson object.

        Args:
            file_path (str): Path to the JSON file used for storing movies.
        """
        self.file_path = file_path

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                json.dump({}, file)

        print(f"[INFO] Storage ready: {self.file_path}")

    def _load_data(self):
        """
        Load movie data from the JSON file.

        Returns:
            dict: Dictionary containing all stored movie data.
        """
        try:
            with open(self.file_path, "r") as content:
                return json.load(content)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save_data(self, data):
        """
        Save movie data to the JSON file.

        Args:
            data (dict): The dictionary of movies to be saved.

        Returns:
            None
        """
        try:
            json_data = json.dumps(data, indent=4)
        except TypeError as e:
            print("Error while converting to JSON:", e)
            return

        try:
            with open(self.file_path, 'w') as file:
                file.write(json_data)
        except IOError as e:
            print(f"Error while saving the file: {e}")

    def list_movies(self):
        """
        Retrieve all movies from the storage.

        Returns:
            dict: A dictionary of all stored movies.
        """
        return self._load_data()

    def add_movie(self, title, year, rating, poster):
        """
        Add a new movie to the storage.

        Args:
            title (str): The title of the movie.
            year (int): The release year of the movie.
            rating (float): The rating of the movie.
            poster (str): URL or path to the movie poster.

        Returns:
            None
        """
        movies = self._load_data()

        movies[title] = {
            "rating": float(round(rating, 1)),
            "year": year,
            "poster": poster
        }

        self._save_data(movies)
        print(f"Movie '{title}' added successfully.")

    def delete_movie(self, title):
        """
        Delete a movie from the storage by title.

        Args:
            title (str): The title of the movie to delete.

        Returns:
            None
        """
        movies = self._load_data()

        if title in movies:
            del movies[title]
            self._save_data(movies)
            print(f"Movie '{title}' deleted successfully.")
        else:
            print(f"Movie '{title}' does not exist!")

    def update_movie(self, title, rating):
        """
        Update the rating of an existing movie.

        Args:
            title (str): The title of the movie to update.
            rating (float): The new rating to assign.

        Returns:
            None
        """
        movies = self._load_data()

        if title in movies:
            movies[title]["rating"] = float(round(rating, 1))
            self._save_data(movies)
            print(f"Movie '{title}' updated successfully. New rating: {rating}")
        else:
            print(f"Movie '{title}' does not exist!")


if __name__ == "__main__":
    storage = StorageJson("test.json")
    storage.add_movie("Inception", 2010, 8.8, "https://poster.url/inception.jpg")
    print(storage.list_movies())
    storage.delete_movie("Inception")
    print(storage.list_movies())
    storage.add_movie("Inception", 2010, 8.8, "https://poster.url/inception.jpg")
    print(storage.list_movies())
    storage.update_movie("Inception", 9.5)
    print(storage.list_movies())
