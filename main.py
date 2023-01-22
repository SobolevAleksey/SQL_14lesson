from flask import render_template, Blueprint, request, jsonify
import utils

main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route("/movie/<title>")
def get_by_title(title):
    query = f"""
    SELECT * FROM 'netflix.db' WHERE `title` = {title} ORDER BY `date_added` DESC
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
