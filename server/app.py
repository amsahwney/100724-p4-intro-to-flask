#!/usr/bin/env python3

from flask import make_response, jsonify, request
from config import app

@app.get('/')
def index():
    return make_response( "<h1>Hello World</h1>" )

@app.get('/welcome')
def welcome():
    return make_response('<h2>Welcome!</h2><p>This is my website</p>')

@app.get("/tv-shows")
def all_shows():
    tv_shows = [
        {"name": "Warehouse Wars"},
        {"name": "One Piece"},
        {"name": "Teletubbies"}
    ]

    return make_response (jsonify(tv_shows), 200)

@app.post('/tv-shows')
def post_tv_shows():
    new_show = request.json

    print( new_show )

    return f"<h1>CONGRATS YOU MADE A POST REQUEST!</h1><p>Your new show is {new_show['name']} with a rating of {new_show['rating']}</p>"

# int can be integer or string, can have multiple ints in a route
# id can be hamburger
# but the hamburgers have to match (in line 35 and 36)
@app.get('/tv-shows/<int:id>')
def tv_show_page(id):
    return f"You're looking for a show with id {id}"


if __name__ == '__main__':
    app.run(port=5555, debug=True)
