"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaalqm7avj5o496qcs0-a.oregon-postgres.render.com",
        database="todo_3k2d",
        user="todo_3k2d_user",
        password="JVsrOUMgdACdv4U4nyukXwwMaXBdN9Q6")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
