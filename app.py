from flask import Flask
from flask import send_file
from flask import jsonify

app = Flask("movies-api")

@app.route("/movies")
def get_movie():
    return jsonify({
        "title": "Inception",
        "genre": "Sci-Fi",
        "year": 2010
    })

@app.route("/")
# METHOD = GET by default
def home():
    return send_file("index.html")

@app.route("/about")
def about():
    return "About this movies API"

if __name__ == "__main__":
    app.run(debug=True)