import os
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Get the path to the database file in the "instance" folder
database_path = os.path.join(app.instance_path, 'database.db')

# Route to display the admin panel


@app.route('/')
def index():
    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Fetch data from the database tables
    cursor.execute('SELECT * FROM user')
    users = cursor.fetchall()

    cursor.execute('SELECT * FROM followers')
    followers = cursor.fetchall()

    cursor.execute('SELECT * FROM message')
    messages = cursor.fetchall()

    cursor.execute('SELECT * FROM post')
    posts = cursor.fetchall()

    cursor.execute('SELECT * FROM comment')
    comments = cursor.fetchall()

    # Close the connection
    conn.close()

    # Render the admin panel template with the fetched data
    return render_template('admin_panel.html', users=users, followers=followers, messages=messages, posts=posts, comments=comments)


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
