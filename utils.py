import sqlite3


def get_all(query):
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        result = []

        for movie in connection.execute(query).fetchall():
            result.append(movie)


        return result


def get_one(query):
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(query).fetchone()

        if result is None:
            return None
        else:
            return result
