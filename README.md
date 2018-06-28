# User Retrieval Endpoint
Retrieve user information in a Postgres database, using a Flask server.
The information is retreived in a JSON format.

### Running
To run the app, the flask server must be started. If run locally, the database connection settings must be changed in order to run.

The app is deployed through Heroku: https://polar-ridge-13855.herokuapp.com/ (might change over time).

**There are 2 Endpoints:**
- Retrieve all the users in the database: "/users"
- Retrieve one user according to user_id: "/users/[user_id]"

There are only 6 users in the database, so the user_id only goes from 1 to 6.

### Additional information
helper_db.py contains functions to retrieve information from the database.
scripts/preparedb.py is the script that was used to prepare the data and insert it into the Postgres database.
scripts/data.tsv contains the user information in a csv format to be written to the database.

### References
- http://flask.pocoo.org/docs/0.12/quickstart/
- https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04
- https://stackoverflow.com/questions/13081532/return-json-response-from-flask-view
