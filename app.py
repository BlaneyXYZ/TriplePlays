import json

from flask import Flask, render_template
from flask import redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
CONFIG_FILE = json.loads(open("config.json").read())

app.config['MYSQL_HOST'] = CONFIG_FILE['host']
app.config['MYSQL_USER'] = CONFIG_FILE['user']
app.config['MYSQL_PASSWORD'] = CONFIG_FILE['password']
app.config['MYSQL_DB'] = CONFIG_FILE['database']

mysql = MySQL(app)

@app.route('/')
def songs_table():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM view_song_count")
        data = cursor.fetchall()
        print(data)
        return render_template("songs_table.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/artists')
def artists_table():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM view_artists")
        data = cursor.fetchall()
        #print(data)
        return render_template("artists_table.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/artist/<artist_id>')
def artist_info(artist_id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM table_artists WHERE artist_id = %s", [artist_id])
        data = cursor.fetchall()
        print(data)
        return render_template("artist_page.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/git')
def gitlink():
    return redirect("https://github.com/BlaneyXYZ/TriplePlays")


if __name__ == '__main__':
    app.run()
