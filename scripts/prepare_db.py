import psycopg2
import csv
import os


def prepare_data(input_file):
    """Convert an input file containing user info into structured data.

    Args:
        input_file (str): path to input CSV file.

    Returns:
        list: a list of tupples contaning the user's first and last name.
    """
    users = []
    with open(input_file) as infile:
        reader = csv.reader(infile)
        for line in reader:
            first_name = line[1]
            last_name = line[2]
            users.append((first_name, last_name))
    return users


def insert_user(first_name, last_name, cursor):
    """Insert a user into the database.

    Args:
        first_name (str): the user's first name.
        last_name (str): the user's last name.
        cursor (psycopg2.connect.cursor): the database connection cursor.
    """
    query = """INSERT INTO users (first_name, last_name)
               VALUES ('{}', '{}');""".format(first_name, last_name)

    print("Inserting user {} {}".format(first_name, last_name))
    cursor.execute(query)


def create_default_table(cursor):
    """Create the default user database.

    Args:
        cursor (psycopg2.connect.cursor): the database connection cursor.
    """
    query = """CREATE TABLE users (
               user_id serial PRIMARY KEY,
               first_name varchar (50) NOT NULL,
               last_name varchar (50) NOT NULL);"""

    cursor.execute(query)


if __name__ == '__main__':
    """Prepare the input data and write to the database."""

    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()

    create_default_table(cur)
    users = prepare_data("data.tsv")
    for user in users:
        insert_user(user[0], user[1], cur)

    cur.close()
    conn.commit()
