from fetch_movie import fetch_movie_data
from helpers import *


class MovieApp:
    """Main application class for managing movies using a storage backend."""

    def __init__(self, storage, title="My Movie Database"):
        """
        Initialize the MovieApp.

        Args:
            storage (IStorage): The storage backend to use (e.g., StorageJson).
            title (str): The title to display in the UI.
        """
        self._storage = storage
        self._title = title

    def _command_list_movies(self):
        """
        List all movies stored in the database.

        Returns:
            None
        """
        movies = self._storage.list_movies()
        show_movies(movies)

    def _command_add_movie(self):
        """
        Prompts the user for a movie title, fetches movie data from the OMDb API,
        and adds the movie to storage if it does not already exist.

        The stored movie includes:
        - Title (as provided by the user)
        - Year (from API)
        - IMDb rating (from API, 0.0 if not available)
        - Poster URL (from API)

        If the movie already exists in the storage with the same title and year,
        the movie is not added again.

        :return: None
        """
        movies = self._storage.list_movies()
        title = get_title_from_user()
        data = fetch_movie_data(title)
        if data:
            year = int(data.get("Year"))
            if title in movies and movies.get(title).get("year") == year:
                print(f"\nMovie '{title}' already exists!")
            else:
                rating = float(data.get("imdbRating")) if data.get("imdbRating") != "N/A" else 0.0
                poster = data.get("Poster")
                self._storage.add_movie(title, year, rating, poster)

    def _command_delete_movie(self):
        """
        Prompt the user to delete a movie by title.

        Returns:
            None
        """
        movies = self._storage.list_movies()
        movie_to_delete = get_title_from_user()
        if movie_to_delete in movies:
            self._storage.delete_movie(movie_to_delete)
        else:
            print(f"\nMovie '{movie_to_delete}' doesn't exist!")

    def _command_update_movie(self):
        """
        Prompt the user to update the rating of an existing movie.

        Returns:
            None
        """
        movies = self._storage.list_movies()
        movie_name = get_title_from_user()
        if movie_name in movies:
            new_movie_rating = get_valid_rating_from_user()
            self._storage.update_movie(movie_name, new_movie_rating)
        else:
            print(f"\nMovie '{movie_name}' doesn't exist!")

    def _command_movie_stats(self):
        """
        Calculate and display statistics about the stored movies.

        Returns:
            None
        """
        movies = self._storage.list_movies()
        average = get_average_rating(movies)
        median = get_median_rating(movies)
        best_movies = get_best_rated_movies(movies)
        worst_movies = get_worst_rated_movies(movies)
        display_movie_stats(average, median, best_movies, worst_movies)

    def _command_random_movie(self):
        """
        Display a randomly selected movie from the database.

        Returns:
            None
        """
        movies = self._storage.list_movies()
        movie = get_random_movie(movies)
        display_random_movie(movie)

    def _command_search_movie(self):
        """
        Prompt the user for a search term and display matching movies.

        Returns:
            None
        """
        movies = self._storage.list_movies()
        found_movies = find_movies(movies)
        display_found_movies(found_movies)

    def _command_sort_by_rating(self):
        """
        Prompt the user for sort order and display movies sorted by rating.

        Returns:
            None
        """
        movies = self._storage.list_movies()
        order = ask_user_for_sequence()
        sorted_movies = sort_movies_by_rating(movies, order)
        show_movies(sorted_movies)

    def _command_sort_by_year(self):
        """
        Prompt the user for sort order and display movies sorted by year.

        Returns:
            None
        """
        movies = self._storage.list_movies()
        order = ask_user_for_sequence()
        sorted_movies = sort_movies_by_year(movies, order)
        show_movies(sorted_movies)

    def _command_filter_movies(self):
        """
        Filter movies based on user-defined rating and year range.

        Returns:
            None
        """
        movies = self._storage.list_movies()
        min_rating = get_minimum_rating_from_user()
        start_year = get_start_year_from_user()
        end_year = get_end_year_from_user()
        filtered = filter_movies(movies, min_rating, start_year, end_year)
        show_movies(filtered)

    def _generate_website(self):
        """
        Placeholder method for generating a website (not implemented yet).

        Returns:
            None
        """
        print("\nWebsite generation is not implemented yet.")

    def run(self):
        """
        Start the main loop of the movie app, display the menu, and handle commands.

        Returns:
            None
        """
        print_title(self._title)
        while True:
            print_menu(menu)
            user_choice = ask_for_valid_number(menu)

            match user_choice:
                case 0:
                    print("\nBye Bye!")
                    break
                case 1:
                    self._command_list_movies()
                    press_enter_to_continue()
                case 2:
                    self._command_add_movie()
                    press_enter_to_continue()
                case 3:
                    self._command_delete_movie()
                    press_enter_to_continue()
                case 4:
                    self._command_update_movie()
                    press_enter_to_continue()
                case 5:
                    self._command_movie_stats()
                    press_enter_to_continue()
                case 6:
                    self._command_random_movie()
                    press_enter_to_continue()
                case 7:
                    self._command_search_movie()
                    press_enter_to_continue()
                case 8:
                    self._command_sort_by_rating()
                    press_enter_to_continue()
                case 9:
                    self._command_sort_by_year()
                    press_enter_to_continue()
                case 10:
                    self._command_filter_movies()
                    press_enter_to_continue()
