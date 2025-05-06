from movie_app import MovieApp
from storage.storage_csv import StorageCsv
from storage.storage_json import StorageJson


def main():
    storage = StorageCsv("data/movies.csv")
    storage = StorageJson("data/movies.json")
    app = MovieApp(storage, "Lukas's Movies")
    app.run()


if __name__ == "__main__":
    main()
