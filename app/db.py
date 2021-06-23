import sqlite3

import click
from flask import current_app, g #g stores data to be accessed by multiple functions, current_app points to your flask app
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        # establish a connection to file pointed at by DATABASE
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row # return rows that behave like dicts

    return g.db

# check if a connection has been created. If so, close it
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()