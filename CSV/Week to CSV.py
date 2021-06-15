import json, datetime, csv
from urllib.request import urlopen
#2021-03-15T13:00:00Z
base_date = datetime.date(2021, 5, 23)

to_date = (base_date.strftime("%Y-%m-%dT13:00:00Z"))
from_date = (base_date - datetime.timedelta(days=8)).strftime("%Y-%m-%dT13:00:00Z")
songs_url = urlopen("https://music.abcradio.net.au/api/v1/recordings/plays.json?order=desc&offset=100&service=triplej&from={}&to={}".format(from_date, to_date))
text = json.loads(jsonurl.read())
title = ""
artist = ""
ranking = 1

print(to_date)
print(from_date)

for i in text['items']:
    title = (i['title'])
    for a in i['artists']:
        artist = (a['name'])
    print("#{} {}-{}".format(ranking, title, artist))
    ranking+=1