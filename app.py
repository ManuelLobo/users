import os
import psycopg2
from flask import Flask, jsonify, render_template
from helper_db import get_users, get_user_by_id

app = Flask(__name__)

# Database connection
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

@app.route('/')
def index():
    #return 'User databse page!'
    return render_template("index.html")


@app.route('/users')
def users():
    """Retrieve all the users in the database, in a JSON format."""
    users = get_users(cur)

    user_list = []
    for user in users:
        first_name = user[0]
        last_name = user[1]
        user_list.append({"first_name": first_name, "last_name": last_name})

    return jsonify(user_list)


@app.route('/users/<user_id>')
def show_user_profile(user_id):
    """Retrieve a single user in the database, using the user_id, in a
    JSON format.
    """
    user = get_user_by_id(user_id, cur)
    first_name = user[0]
    last_name = user[1]
    user_object = {"first_name": first_name, "last_name": last_name}

    return jsonify(user_object)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
