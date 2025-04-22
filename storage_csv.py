import csv
import os

from istorage import IStorage


class StorageCsv(IStorage):
    """CSV-based implementation of the IStorage interface for managing movie data."""

    def __init__(self, file_path):
        """
        Initialize the StorageCsv object and ensure the CSV file exists.

        Args:
            file_path (str): Path to the CSV file used for storing movies.
        """
        self.file_path = file_path

        if not os.path.exists(self.file_path):
            with open(self.file_path, mode="w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["title", "rating", "year", "poster"])

        print(f"[INFO] Storage ready: {self.file_path}")

    def _load_data(self):
        """
        Load movie data from the CSV file.

        Returns:
            dict: Dictionary containing all stored movie data.
        """
        movies = {}
        try:
            with open(self.file_path, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    movies[row["title"]] = {
                        "rating": float(row["rating"]),
                        "year": int(row["year"]),
                        "poster": row["poster"]
                    }
        except FileNotFoundError:
            return {}

        return movies

    def _save_data(self, movies):
        """
        Save the entire movie dictionary into the CSV file.

        Args:
            movies (dict): The movies to save.

        Returns:
            None
        """
        with open(self.file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["title", "rating", "year", "poster"])  # Header
            for title, data in movies.items():
                writer.writerow([title, data["rating"], data["year"], data["poster"]])

    def list_movies(self):
        """
        Retrieve all movies from the CSV file.

        Returns:
            dict: Movies in the format {title: {rating, year, poster}}
        """
        return self._load_data()

    def add_movie(self, title, year, rating, poster):
        """
        Add a new movie to the CSV storage.

        Args:
            title (str): Movie title.
            year (int): Release year.
            rating (float): Movie rating.
            poster (str): Poster URL or path.

        Returns:
            None
        """
        movies = self.list_movies()
        movies[title] = {
            "rating": float(round(rating, 1)),
            "year": year,
            "poster": poster
        }
        self._save_data(movies)
        print(f"Movie '{title}' added successfully.")

    def delete_movie(self, title):
        """
        Delete a movie from the CSV storage by its title.

        Args:
            title (str): The title of the movie to delete.

        Returns:
            None
        """
        movies = self.list_movies()
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
        movies = self.list_movies()
        if title in movies:
            movies[title]["rating"] = float(round(rating, 1))
            self._save_data(movies)
            print(f"Movie '{title}' updated successfully. New rating: {rating}")
        else:
            print(f"Movie '{title}' does not exist!")


if __name__ == "__main__":
    # test functions
    storage = StorageCsv("test.csv")
    movies = storage.list_movies()
    print(movies)
    storage.add_movie("The Matrix", 1999, 8.7, "https://poster/matrix.jpg")
    print(storage.list_movies())
    storage.delete_movie("The Matrix")
    print(storage.list_movies())
    storage.add_movie("The Matrix", 1999, 8.7, "https://poster/matrix.jpg")
    print(storage.list_movies())
    storage.update_movie("The Matrix", 9.2)
    print(storage.list_movies())
