# TriplePlays
Pulling the most played songs on triplej from [here](https://www.abc.net.au/triplej/featured-music/most-played/) once a week and building a database for me to make predictions with for Hottest 100
#### Nothing special yet :(
## Screenshots
![Screenshot of current state](http://scr.blny.me/scr/chrome_2021-08-23_22-07-23.png)

## Setup
Not sure why you would want to use it currently but gg

1. Install the python dependencies using `pip` using the following command in the root directory:
```
pip install -r requirements.txt
```

2. Create the required MYSQL tables using tripleplays_table_songs.csv and tripleplays_table_artists.csv

3. Rename config-sample.json to config.json and modify it with the MYSQL details
```
{
  "host": "mysql.you.suck",
  "user": "tripleplays",
  "password": "heheno",
  "database": "tripleplays"
}
```

4. Modify Extras\update_all.py to set the start and end dates for updating the DB with a set period, then run it
```
python3 update_all.py
```

5. Modify Extras\update.py to set the period desired i.e past week
```
python3 update.py
```

6. Start app.py to view the interface
```
python3 app.py
```

