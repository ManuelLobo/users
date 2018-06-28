import psycopg2
from flask import Flask, jsonify
from helper_db import get_users, get_user_by_id
import os
app = Flask(__name__)

#conn = psycopg2.connect(host="localhost",database="post_db", user="postgres", password="post123")
#cur = conn.cursor()
#DATABASE_URL = os.environ['DATABASE_URL']

#conn = psycopg2.connect(DATABASE_URL, sslmode='require')

@app.route('/')
def hello_world():
    print("asjasajs")
    return 'Hello, World!'


@app.route('/users')
def users():
    users = get_users(cur)
    #print("hahaha")
    #return str(users)

    d = []
    for user in users:
        first_name = user[0]
        last_name = user[1]
        d.append({"first_name": first_name, "last_name": last_name})

    return jsonify(d)



@app.route('/users/<user_id>')
def show_user_profile(user_id):
    user = get_user_by_id(user_id, cur)
    first_name = user[0]
    last_name = user[1]
    d = {"first_name": first_name, "last_name": last_name}
    # show the user profile for that user

    return jsonify(d) #"{} {}".format(first_name, last_name)


#cur.close()
#conn.commit()
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
