from flask import Flask
from flask import send_file
from flask import jsonify
from flask import request

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
    director = request.args.get("director")

    if director is None:
        result = movies
    else:
        result = [m for m in movies if m["director"] == director]

    return jsonify(result)

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