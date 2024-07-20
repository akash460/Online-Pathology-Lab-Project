import os
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST', '127.0.0.1'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', ''),
            database=os.getenv('DB_NAME', 'project')
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

# Additional routes and logic go here
# Example route
@app.route('/login')
def login():
    return render_template('alogin.html')

if __name__ == '__main__':
    app.run(debug=True)
