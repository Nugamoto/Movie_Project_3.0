# 🎬 Movie Project 3.0

**Movie Project 3.0** is a modular, object-oriented Python application that allows users to manage and enrich a list of movies using the [OMDb API](https://www.omdbapi.com/). It includes functionality for reading/writing movie data from various formats and generates a static HTML website to present the results.

This project was created as a portfolio showcase to demonstrate clean code, software architecture principles, API integration, CLI development, and static site generation.

---

## 🚀 Features

- 🔍 Fetch movie data from the OMDb API
- 💾 Read/write data from/to CSV and JSON formats
- 🧩 Interface-based storage abstraction (via `IStorage`)
- ⚙️ CLI-based user interaction (add, list, analyze movies)
- 🖥️ Generates a clean static HTML website using a template
- 🔐 Uses `.env` file to securely store the API key

---

## 🛠️ Technologies Used

- Python 3
- [OMDb API](https://www.omdbapi.com/)
- `python-dotenv`
- CSV, JSON
- HTML/CSS (static output)
- Object-Oriented Programming (OOP)

---

## 📁 Project Structure

```
Movie_Project_3.0/
├── data/
│   ├── movies.csv               # CSV storage file
│   └── movies.json              # JSON storage file
├── static/
│   ├── index_template.html      # HTML template for static site
│   └── style.css                # Basic styling
├── storage/
│   ├── istorage.py              # Storage interface definition
│   ├── storage_csv.py           # CSV storage implementation
│   └── storage_json.py          # JSON storage implementation
├── .gitignore                   # Ignored files
├── fetch_movie.py              # OMDb API logic
├── helpers.py                  # HTML generation and helper functions
├── main.py                     # Application entry point
├── movie_app.py                # Core app logic and CLI
└── README.md                   # Project documentation
```

---

## ⚙️ Setup & Usage

### 1. Clone the repository

```bash
git clone https://github.com/Nugamoto/Movie_Project_3.0.git
cd Movie_Project_3.0
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

If no `requirements.txt` is provided, manually install:

```bash
pip install python-dotenv requests
```

### 3. Configure API Key

Create a `.env` file in the root directory with:

```env
OMDB_API_KEY=your_api_key_here
```

You can get your API key at [omdbapi.com/apikey.aspx](https://www.omdbapi.com/apikey.aspx)

### 4. Run the app

```bash
python main.py
```

Follow the CLI prompts to add movies, choose a storage format, or generate the website.

### 5. View Static Website

After generation, open `static/index.html` in a web browser to view your movie list.

---

## 🌐 Example Use Cases

- Build and manage a personal movie watchlist
- Fetch movie metadata like ratings, plots, actors
- Analyze your collection and generate a sharable website
- Practice API usage and object-oriented design in Python

---

## 📸 Screenshots

*Add screenshots of the CLI and the generated HTML site here for visual reference.*

---

## 🧠 What This Project Demonstrates

- Clean modular architecture using OOP and interfaces
- External API integration using `requests`
- Secure credential handling using `.env`
- Data persistence with multiple file formats
- Static site generation with template substitution
- CLI application development in Python

---

## 📝 License

This project is licensed under the MIT License.

---

> Made with ❤️ by [Nugamoto](https://github.com/Nugamoto)
