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
    print(f"\n********** {title} **********")


def print_menu(menu_list):
    print("\nMenu:")
    for number, element in enumerate(menu_list):
        print(f"{number}. {element}")
    print("\n")


def ask_for_valid_number(menu_list):
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
    input("\nPress enter to continue: ")


def show_movies(movies):
    if not movies:
        print("No movies found!")
    else:
        print(f"\n----- Total of {len(movies)} movies -----")
        for title, data in movies.items():
            print(f"'{title}'\n\tRating: {float(data['Rating'])} | Year: {data['Year of release']} ")


def get_average_rating(movies):
    ratings = [details["Rating"] for details in movies.values()]
    return round(sum(ratings) / len(ratings), 1) if ratings else None


def get_median_rating(movies):
    ratings = sorted([details["Rating"] for details in movies.values()])
    return round(statistics.median(ratings), 1) if ratings else None


def get_best_rated_movies(movies):
    best_rated_movies = []
    best_rating = MIN_RATING

    for movie, data in movies.items():
        if data["Rating"] > best_rating:
            best_rated_movies = [(movie, data["Rating"])]
            best_rating = data["Rating"]
            continue
        if data["Rating"] == best_rating:
            best_rated_movies.append((movie, data["Rating"]))

    return best_rated_movies if best_rated_movies else []


def get_worst_rated_movies(movies):
    worst_rated_movies = []
    worst_rating = MAX_RATING

    for movie, data in movies.items():
        if data["Rating"] < worst_rating:
            worst_rated_movies = [(movie, data["Rating"])]
            worst_rating = data["Rating"]
            continue
        if data["Rating"] == worst_rating:
            worst_rated_movies.append((movie, data["Rating"]))

    return worst_rated_movies if worst_rated_movies else []


def get_random_movie(movies):
    random_movie_name = choice(list(movies))
    random_movie_data = movies[random_movie_name]
    return random_movie_name, random_movie_data


def find_movies(movies):
    part_of_movie_name = input("Enter part of movie name: ")
    found_items = {}
    for title, data in movies.items():
        if part_of_movie_name.lower() in title.lower():
            found_items[title] = data
    return found_items


def sort_movies_by_rating(movies, order):
    sorted_movies = dict(sorted(movies.items(), key=lambda item: item[1]["Rating"], reverse=order))
    return sorted_movies


def get_title_from_user():
    return input("Enter movie name: ")


def get_valid_year_from_user():
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
    sorted_movies = dict(sorted(movies.items(), key=lambda item: item[1]["Year of release"], reverse=order))
    return sorted_movies


def ask_user_for_sequence():
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
    print("\n")
    if not found_movies:
        print(f"No movie found.")
    else:
        show_movies(found_movies)


def display_random_movie(random_movie):
    print(f"\n"
          f"Your movie for tonight:\n"
          f"'{random_movie[0]}'\nIt's rated {float(random_movie[1]['Rating'])} "
          f"and released {random_movie[1]['Year of release']}.")


def get_minimum_rating_from_user():
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
    movies_by_rating = sort_movies_by_rating(movies, True)
    filtered_movies = {}
    for title, data in movies_by_rating.items():
        if data["Rating"] >= min_rating and start_year <= data["Year of release"] <= end_year:
            filtered_movies[title] = data
    return filtered_movies
