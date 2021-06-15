import json, datetime, csv
from urllib.request import urlopen
import mysql.connector
#2021-03-15T13:00:00Z
base_date = datetime.date(2021, 6, 13)

to_date = (base_date.strftime("%Y-%m-%dT13:00:00Z"))
from_date = (base_date - datetime.timedelta(days=8)).strftime("%Y-%m-%dT13:00:00Z")
jsonurl = urlopen("https://music.abcradio.net.au/api/v1/recordings/plays.json?order=desc&limit=100&service=triplej&from={}&to={}".format(from_date, to_date))
text = json.loads(jsonurl.read())
title = ""
artist = ""
ranking = 1
CONFIG_FILE = json.loads(open("../config.json").read())
mydb = mysql.connector.connect(
    host=CONFIG_FILE['host'],
    user=CONFIG_FILE['user'],
    password=CONFIG_FILE['password'],
    database=CONFIG_FILE['database']
)
mycursor = mydb.cursor()

check_artist_sql = "SELECT * FROM table_artists WHERE artist_name LIKE %s LIMIT 1"
add_artist_sql = "INSERT INTO table_artists (artist_name) VALUES (%s)"
check_song_sql = "SELECT * FROM table_songs WHERE song_name LIKE %s LIMIT 1"
add_song_sql = "INSERT INTO table_songs (song_name, song_artist) VALUES (%s, %s)"
modify_song_count = "UPDATE table_songs SET song_count = song_count + 1 WHERE song_id = %s"
def checkArtist(artist_name):
    mycursor.execute(check_artist_sql, (artist_name,))
    row = mycursor.fetchone()
    print(row)
    if row is None:
        print("adding {} to table_artists".format(artist_name))
        mycursor.execute(add_artist_sql, (artist_name,))
        mydb.commit()
        return(mycursor.lastrowid)
    else:
        return(row[0])

def checkSong(artist_id, song_name):
    mycursor.execute(check_song_sql, (song_name,))
    row = mycursor.fetchone()
    print(row)
    if row is None:
        print("adding {} to table_songs".format(song_name))
        mycursor.execute(add_song_sql, (song_name, artist_id,))
        mydb.commit()
        return(mycursor.lastrowid)
    else:
        mycursor.execute(modify_song_count, (row[0],))
        mydb.commit()
        return(row[0])

# iterate through JSON
for i in text['items']:
    title = (i['title'])
    for a in i['artists']:
        artist = (a['name'])
    print("#{} {}-{}".format(ranking, title, artist))
    checkSong(checkArtist(artist), title)
    ranking+=1