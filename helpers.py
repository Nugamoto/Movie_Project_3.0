import statistics
from random import choice

__all__ = [
    "menu",
    "print_title",
    "print_menu",
    "ask_for_valid_number",
    "press_enter_to_continue",
    "show_movies",
    "get_average_rating",
    "get_median_rating",
    "get_best_rated_movies",
    "get_worst_rated_movies",
    "get_random_movie",
    "find_movies",
    "sort_movies_by_rating",
    "get_title_from_user",
    "get_valid_year_from_user",
    "get_valid_rating_from_user",
    "sort_movies_by_year",
    "ask_user_for_sequence",
    "display_movie_stats",
    "display_found_movies",
    "display_random_movie",
    "get_minimum_rating_from_user",
    "get_start_year_from_user",
    "get_end_year_from_user",
    "filter_movies"
]

MIN_YEAR = 1000
MAX_YEAR = 9999

MIN_RATING = 0.0
MAX_RATING = 10.0

menu = ("Exit",
        "List movies",
        "Add movie",
        "Delete movie",
        "Update movie",
        "Stats",
        "Random movie",
        "Search movie",
        "Movies sorted by rating",
        "Movies sorted by year",
        "Filter movies"
        )


def print_title(title: str):
    """
    Print a formatted title.

    Args:
        title (str): The title to be printed.
    """
    print(f"\n********** {title} **********")


def print_menu(menu_list):
    """
    Display the menu options.

    Args:
        menu_list (list): List of menu options to display.
    """
    print("\nMenu:")
    for number, element in enumerate(menu_list):
        print(f"{number}. {element}")
    print("\n")


def ask_for_valid_number(menu_list):
    """
    Prompt the user to select a valid menu option.

    Args:
        menu_list (list): List of menu options.

    Returns:
        int: The valid menu option selected by the user.
    """
    final_digit = len(menu_list) - 1
    while True:
        try:
            number = int(input(f"Enter choice (0-{final_digit}): "))
            if 0 <= number <= final_digit:
                return number
            print(f"The choice must be between 0 and {final_digit}. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number!")


def press_enter_to_continue():
    """
    Pause execution until the user presses Enter.
    """
    input("\nPress enter to continue: ")


def show_movies(movies):
    """
    Display a list of movies with their ratings and release years.

    Args:
        movies (dict): Dictionary of movies with title as key and details as value.
    """
    if not movies:
        print("No movies found!")
    else:
        print(f"\n----- Total of {len(movies)} movies -----")
        for title, data in movies.items():
            print(f"'{title}'\n\tRating: {float(data['rating'])} | Year: {data['year']} ")


def get_average_rating(movies):
    """
    Calculate the average rating of movies.

    Args:
        movies (dict): Dictionary of movies.

    Returns:
        float or None: Average rating rounded to 1 decimal place, or None if no movies.
    """
    ratings = [details["rating"] for details in movies.values()]
    return round(sum(ratings) / len(ratings), 1) if ratings else None


def get_median_rating(movies):
    """
    Calculate the median rating of movies.

    Args:
        movies (dict): Dictionary of movies.

    Returns:
        float or None: Median rating rounded to 1 decimal place, or None if no movies.
    """
    ratings = sorted([details["rating"] for details in movies.values()])
    return round(statistics.median(ratings), 1) if ratings else None


def get_best_rated_movies(movies):
    """
    Find the movie(s) with the highest rating.

    Args:
        movies (dict): Dictionary of movies.

    Returns:
        list: List of tuples containing movie title and rating.
    """
    best_rated_movies = []
    best_rating = MIN_RATING

    for movie, data in movies.items():
        if data["rating"] > best_rating:
            best_rated_movies = [(movie, data["rating"])]
            best_rating = data["rating"]
            continue
        if data["rating"] == best_rating:
            best_rated_movies.append((movie, data["rating"]))

    return best_rated_movies if best_rated_movies else []


def get_worst_rated_movies(movies):
    """
    Find the movie(s) with the lowest rating.

    Args:
        movies (dict): Dictionary of movies.

    Returns:
        list: List of tuples containing movie title and rating.
    """
    worst_rated_movies = []
    worst_rating = MAX_RATING

    for movie, data in movies.items():
        if data["rating"] < worst_rating:
            worst_rated_movies = [(movie, data["rating"])]
            worst_rating = data["rating"]
            continue
        if data["rating"] == worst_rating:
            worst_rated_movies.append((movie, data["rating"]))

    return worst_rated_movies if worst_rated_movies else []


def get_random_movie(movies):
    """
    Select a random movie from the collection.

    Args:
        movies (dict): Dictionary of movies.

    Returns:
        tuple: Movie title and its details.
    """
    random_movie_name = choice(list(movies))
    random_movie_data = movies[random_movie_name]
    return random_movie_name, random_movie_data


def find_movies(movies):
    """
    Search for movies containing a user-provided substring.

    Args:
        movies (dict): Dictionary of movies.

    Returns:
        dict: Movies matching the search criteria.
    """
    part_of_movie_name = input("Enter part of movie name: ")
    found_items = {}
    for title, data in movies.items():
        if part_of_movie_name.lower() in title.lower():
            found_items[title] = data
    return found_items


def sort_movies_by_rating(movies, order):
    """
    Sort movies by rating.

    Args:
        movies (dict): Dictionary of movies.
        order (bool): True for descending, False for ascending.

    Returns:
        dict: Sorted dictionary of movies.
    """
    sorted_movies = dict(sorted(movies.items(), key=lambda item: item[1]["rating"], reverse=order))
    return sorted_movies


def get_title_from_user():
    """
    Prompt user to enter a movie title.

    Returns:
        str: Movie title entered by the user.
    """
    return input("Enter movie name: ")


def get_valid_year_from_user():
    """
    Prompt user to enter a valid year.

    Returns:
        int: Validated year.
    """
    while True:
        try:
            year = int(input("Enter year of release: "))
            if MIN_YEAR <= year <= MAX_YEAR:
                break
            print("Invalid year. Please enter a 4-digit year!")
        except ValueError:
            print("Invalid input. Please enter a valid 4-digit year!")
    return year


def get_valid_rating_from_user():
    """
    Prompt user to enter a valid movie rating.

    Returns:
        float: Validated rating.
    """
    while True:
        try:
            rating = round(float(input("Enter new movie rating (0-10): ")), 1)
            if MIN_RATING <= rating <= MAX_RATING:
                break
            print(f"Rating {rating} is invalid. Please try again!")
        except ValueError:
            print("Invalid input. Please enter a valid number!")
    return rating


def sort_movies_by_year(movies, order):
    """
    Sort movies by release year.

    Args:
        movies (dict): Dictionary of movies.
        order (bool): True for descending, False for ascending.

    Returns:
        dict: Sorted dictionary of movies.
    """
    sorted_movies = dict(sorted(movies.items(), key=lambda item: item[1]["year"], reverse=order))
    return sorted_movies


def ask_user_for_sequence():
    """
    Ask user to choose sorting sequence.

    Returns:
        bool: False for ascending, True for descending.
    """
    while True:
        sequence = input(f"\nEnter '1' for ascending sequence.\n"
                         f"Enter '2' for descending sequence.\n")
        if sequence == "1":
            return False
        elif sequence == "2":
            return True
        else:
            print(f"Bad input! Please enter '1' or '2'.")


def display_movie_stats(average, median, best_movies, worst_movies):
    """
    Display statistics about movies.

    Args:
        average (float): Average rating.
        median (float): Median rating.
        best_movies (list): List of best rated movies.
        worst_movies (list): List of worst rated movies.
    """
    print(f"\n"
          f"----- Stats -----"
          f"\n"
          f"Average rating: {average}\n"
          f"Median rating : {median}")
    if len(best_movies) == 1:
        print(f"Best movie    : '{best_movies[0][0]}', Rating: {best_movies[0][1]}")
    else:
        print(f"Best movies   : - '{best_movies[0][0]}', Rating: {best_movies[0][1]}")
        for best_movie in best_movies[1:]:
            print(f"                - '{best_movie[0]}', Rating: {best_movie[1]}")
    if len(worst_movies) == 1:
        print(f"Worst movie   : '{worst_movies[0][0]}', Rating: {worst_movies[0][1]}")
    else:
        print(f"Worst movies  : - '{worst_movies[0][0]}', Rating: {worst_movies[0][1]}")
        for worst_movie in worst_movies[1:]:
            print(f"                - '{worst_movie[0]}', Rating: {worst_movie[1]}")


def display_found_movies(found_movies):
    """
    Display movies found by search.

    Args:
        found_movies (dict): Dictionary of found movies.
    """
    print("\n")
    if not found_movies:
        print(f"No movie found.")
    else:
        show_movies(found_movies)


def display_random_movie(random_movie):
    """
    Display details of a randomly selected movie.

    Args:
        random_movie (tuple): Movie title and details.
    """
    print(f"\n"
          f"Your movie for tonight:\n"
          f"'{random_movie[0]}'\nIt's rated {float(random_movie[1]['rating'])} "
          f"and released {random_movie[1]['year']}.")


def get_minimum_rating_from_user():
    """
    Prompt user to enter a minimum rating or leave blank for default.

    Returns:
        float: Minimum rating.
    """
    while True:
        try:
            rating = input("Enter minimum rating (0-10) or leave blank for no minimum rating: ")
            if not rating:
                return MIN_RATING
            valid_rating = round(float(rating), 1)
            if MIN_RATING <= valid_rating <= MAX_RATING:
                break
            print(f"Rating {valid_rating} is invalid. Please try again!")
        except ValueError:
            print("Invalid input. Please enter a valid number or leave blank!")
    return valid_rating


def get_start_year_from_user():
    """
    Prompt user to enter a start year or leave blank for default.

    Returns:
        int: Start year.
    """
    while True:
        try:
            year = input("Enter start year or leave blank for no start year: ")
            if year == "":
                return MIN_YEAR
            valid_year = int(year)
            if MIN_YEAR <= valid_year <= MAX_YEAR:
                break
            print(f"Year {valid_year} is invalid. Please enter a 4-digit year!")
        except ValueError:
            print("Invalid input. Please enter a valid 4-digit year or leave blank!")
    return valid_year


def get_end_year_from_user():
    """
    Prompt user to enter an end year or leave blank for default.

    Returns:
        int: End year.
    """
    while True:
        try:
            year = input("Enter end year or leave blank for no end year: ")
            if year == "":
                return MAX_YEAR
            valid_year = int(year)
            if MIN_YEAR <= valid_year <= MAX_YEAR:
                break
            print(f"Year {valid_year} is invalid. Please enter a 4-digit year!")
        except ValueError:
            print("Invalid input. Please enter a valid 4-digit year or leave blank!")
    return valid_year


def filter_movies(movies, min_rating, start_year, end_year):
    """
    Filter movies based on minimum rating and year range.

    Args:
        movies (dict): Dictionary of movies.
        min_rating (float): Minimum rating threshold.
        start_year (int): Start year.
        end_year (int): End year.

    Returns:
        dict: Filtered dictionary of movies.
    """
    movies_by_rating = sort_movies_by_rating(movies, True)
    filtered_movies = {}
    for title, data in movies_by_rating.items():
        if data["rating"] >= min_rating and start_year <= data["year"] <= end_year:
            filtered_movies[title] = data
    return filtered_movies
