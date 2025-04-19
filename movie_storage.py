import json


def get_movies(filepath):
    try:
        with open(filepath, "r") as content:
            return json.load(content)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_movies(movies, filepath):
    with open(filepath, "w") as content:
        content.write(json.dumps(movies))


def add_movie(title, rating, year, filepath):
    movies = get_movies(filepath)

    movies[title] = {
        "rating": float(round(rating, 1)),
        "year": year
    }

    print(f"\nMovie '{title}' (Rating: {rating}, Year: {year}) successfully added")
    save_movies(movies, filepath)


def delete_movie(title, filepath):
    movies = get_movies(filepath)

    if title in movies:
        del movies[title]
        print(f"\nMovie '{title}' successfully deleted")
        save_movies(movies, filepath)
    else:
        print(f"\nMovie '{title}' does not exist!")


def update_movie(title, rating, filepath):
    movies = get_movies(filepath)

    if title in movies:
        movies[title]["rating"] = float(round(rating, 1))
        print(f"\nMovie '{title}' successfully updated")
        save_movies(movies, filepath)
    else:
        print(f"\nMovie '{title}' does not exist!")
