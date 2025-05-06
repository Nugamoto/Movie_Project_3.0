from movie_app import MovieApp
from storage_json import StorageJson
# from storage_csv import StorageCsv

def main():
    storage = StorageJson("movies.json")
    # storage = StorageCsv("movies.csv")
    app = MovieApp(storage, "Lukas's Movies")
    app.run()


if __name__ == "__main__":
    main()
