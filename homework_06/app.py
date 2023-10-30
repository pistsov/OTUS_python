import asyncio
from os import getenv

from flask import Flask, render_template
from flask_migrate import Migrate

import crud
from jsonplaceholder_requests import fetch_users, fetch_posts
from models import db, Post, User
from views.posts import posts_app
from views.users import users_app

app = Flask(__name__)
config_name = getenv("CONFIG_NAME", "DevelopmentConfig")
app.config.from_object(f"config.{config_name}")

db.init_app(app=app)
migrate = Migrate(app=app, db=db)
app.register_blueprint(users_app)
app.register_blueprint(posts_app)


with app.app_context():
    db.drop_all()
    db.create_all()


async def fetch_data():
    users_data, posts_data = await asyncio.gather(
        fetch_users(),
        fetch_posts()
    )
    return [users_data, posts_data]


def populate_data():
    users_data, posts_data = asyncio.run(fetch_data())
    with app.app_context():
        crud.populate_users(users_data=users_data)
        crud.populate_posts(posts_data=posts_data)


@app.get("/", endpoint="index")
def get_index():
    return render_template("index.html")


populate_data()
