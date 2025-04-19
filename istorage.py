from abc import ABC, abstractmethod

class IStorage(ABC):
    """Interface that defines the required methods for a movie storage system."""

    @abstractmethod
    def list_movies(self):
        """
        Retrieve all movies from the storage.

        Returns:
            dict: A dictionary containing all stored movies.
        """
        pass

    @abstractmethod
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
        pass

    @abstractmethod
    def delete_movie(self, title):
        """
        Delete a movie from the storage by title.

        Args:
            title (str): The title of the movie to delete.

        Returns:
            None
        """
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """
        Update the rating of an existing movie.

        Args:
            title (str): The title of the movie to update.
            rating (float): The new rating to assign.

        Returns:
            None
        """
        pass