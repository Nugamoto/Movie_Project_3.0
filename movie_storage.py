import json


def get_movies(filepath="data.json"):
    try:
        with open(filepath, "r") as content:
            return json.load(content)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_movies(movies, filepath="data.json"):
    with open(filepath, "w") as content:
        content.write(json.dumps(movies))


def add_movie(title, rating, year, filepath="data.json"):
    movies = get_movies(filepath)

    movies[title] = {
        "Rating": float(round(rating, 1)),
        "Year of release": year
    }

    print(f"\nMovie '{title}' (Rating: {rating}, Year: {year}) successfully added")
    save_movies(movies, filepath)


def delete_movie(title, filepath="data.json"):
    movies = get_movies(filepath)

    if title in movies:
        del movies[title]
        print(f"\nMovie '{title}' successfully deleted")
        save_movies(movies, filepath)
    else:
        print(f"\nMovie '{title}' does not exist!")


def update_movie(title, rating, filepath="data.json"):
    movies = get_movies(filepath)

    if title in movies:
        movies[title]["Rating"] = float(round(rating, 1))
        print(f"\nMovie '{title}' successfully updated")
        save_movies(movies, filepath)
    else:
        print(f"\nMovie '{title}' does not exist!")
