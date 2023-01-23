from flask import render_template, Blueprint, request, jsonify
import utils

# Создаем блюпринт
main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route("/movie/<title>")
def get_by_title(title):
    query = f"""
    SELECT * FROM 'netflix' WHERE `title` = '{title}' ORDER BY `date_added` DESC
    """
    query_result = utils.get_one(query)
    if query_result is None:
        return jsonify(status=404)

    movie = {
        'title': query_result['title'],
        'country': query_result['country'],
        'release_year': query_result['release_year'],
        'genre': query_result['listed_in'],
        'description': query_result['description']

    }
    return jsonify(movie)


@main_blueprint.route("/movie/<year1>/to/<year2>")
def get_movie_by_year(year1, year2):
    query = f"""
    SELECT * FROM netflix WHERE release_year BETWEEN {year1} and {year2} LIMIT 100
    """
    result = []
    for movie in utlis.get_all(query):
        result.append(
            {'title': movie['title'],
            'release_year': movie['release_year']
            }
        )
    return jsonify(result)


@main_blueprint.route("/movie/rating/<value>")
def get_movie_by_rating(value):
    query = f"""
    SELECT * FROM netflix
    """
    if value == "children":
        query += 'WHERE rating = "G"'
    elif value == "family":
        query += 'WHERE rating = "G" or rating = "PG" or rating = "PG-13"'
    elif value == "adult":
        query += 'WHERE rating = "R" or rating = "NC-17"'
    else:
        return jsonify(status=400)
    
    result = []
    for movie in utils.get_all(query):
        result.append(
            {'title': movie['title'],
             'rating': movie['rating'],
             'description': movie['description']
            }
        )
     return jsonify(result)

@main_blueprint.route("/genre/<genre>")
def get_movie_by_genre(genre):
    query = f"""
    SELECT * FROM netflix WHERE listed_in LIKE '%{genre}%' ORDER BY date_added DESC LIMIT 10
    """
    result = []
    for movie in utils.get_all(query):
        result.append(
            {'title': movie['title'],
             'description': movie['description']
            }
        )
     
    return jsonify(result)

        
    
    

