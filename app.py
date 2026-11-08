from flask import Flask
from flask import send_file
from flask import jsonify

app = Flask("movies-api")

movies = [
    {
        "id": 1,
        "title": "The Matrix",
        "director": "The Wachowskis",
        "year": 1999,
        "watched": True,
    },
    {
        "id": 2,
        "title": "Inception",
        "director": "Christopher Nolan",
        "year": 2010,
        "watched": False,
    },
]


@app.route("/movies", methods=["GET"])
def get_movie():
    return jsonify(movies)

@app.route("/")
# METHOD = GET by default
def home():
    print(movies)
    return send_file("index.html")

@app.route("/about")
def about():
    return "About this movies API"

if __name__ == "__main__":
    app.run(debug=True)