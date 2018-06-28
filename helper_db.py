def get_users(cursor):
    """Connect to database and retrieve the users' first and last names

    Args:
        cursor (psycopg2.connect.cursor): the database connection cursor.

    Returns:
        list: a list of all the users in the database
    """
    query = "SELECT first_name, last_name FROM users;"
    cursor.execute(query)
    users = cursor.fetchall()
    return users


def get_user_by_id(user_id, cursor):
    """Connect to database and retrieve a user's first and last name

    Args:
        user_id (str): the user's identification number in the database.
        cursor (psycopg2.connect.cursor): the database connection cursor.

    Returns:
        tupple: a tupple with first and last name

    """
    query = "SELECT first_name, last_name FROM users WHERE user_id = {};".format(user_id)
    cursor.execute(query)
    user = cursor.fetchone()
    return user
