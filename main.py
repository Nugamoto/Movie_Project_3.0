from functions import *
from movie_storage import get_movies, add_movie, delete_movie, update_movie


def main():
    print_title("My Movie Database")
    while True:
        print_menu(menu)
        user_choice = ask_for_valid_number(menu)

        if user_choice == 0:
            print("\nBye Bye!")
            break

        movies = get_movies()

        match user_choice:
            case 1:
                show_movies(movies)
                press_enter_to_continue()

            case 2:
                new_movie_title = get_title_from_user()
                if new_movie_title not in movies:
                    new_movie_rating = get_valid_rating_from_user()
                    new_movie_year = get_valid_year_from_user()
                    add_movie(new_movie_title, new_movie_rating, new_movie_year)
                else:
                    print(f"\n'{new_movie_title}' already exists.")
                press_enter_to_continue()

            case 3:
                movie_to_delete = get_title_from_user()
                if movie_to_delete in movies:
                    delete_movie(movie_to_delete)
                else:
                    print(f"\nMovie '{movie_to_delete}' doesn't exist!")
                press_enter_to_continue()

            case 4:
                movie_name = get_title_from_user()
                if movie_name in movies:
                    new_movie_rating = get_valid_rating_from_user()
                    update_movie(movie_name, new_movie_rating)
                else:
                    print(f"\nMovie '{movie_name}' doesn't exist!")
                press_enter_to_continue()

            case 5:
                average = get_average_rating(movies)
                median = get_median_rating(movies)
                best_movies = get_best_rated_movies(movies)
                worst_movies = get_worst_rated_movies(movies)
                display_movie_stats(average, median, best_movies, worst_movies)
                press_enter_to_continue()

            case 6:
                movie = get_random_movie(movies)
                display_random_movie(movie)
                press_enter_to_continue()

            case 7:
                found_movies = find_movies(movies)
                display_found_movies(found_movies)
                press_enter_to_continue()

            case 8:
                order = ask_user_for_sequence()
                sorted_movies = sort_movies_by_rating(movies, order)
                show_movies(sorted_movies)
                press_enter_to_continue()

            case 9:
                order = ask_user_for_sequence()
                sorted_movies = sort_movies_by_year(movies, order)
                show_movies(sorted_movies)
                press_enter_to_continue()

            case 10:
                min_rating = get_minimum_rating_from_user()
                start_year = get_start_year_from_user()
                end_year = get_end_year_from_user()
                filtered = filter_movies(movies, min_rating, start_year, end_year)
                show_movies(filtered)
                press_enter_to_continue()


if __name__ == "__main__":
    main()
