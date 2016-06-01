import psycopg2 as db
import json

with open('config.json', 'r') as f:
    config = json.load(f)

conn = db.connect(user=config['dbuser'], database=config['dbname'], host=config['dbhost'], password=config['dbpass']);
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS uber 
	(
		city		TEXT,
		lat	 	FLOAT (8),
		lng		FLOAT (8),
		eta		INTEGER,
		time		TIMESTAMP WITH TIME ZONE NOT NULL,
		holiday		BOOLEAN,
		PRIMARY KEY (lat, lng, time)
	);""")
print "Created table 'uber' successfully!\n"

cur.execute("""CREATE TABLE IF NOT EXISTS lyft 
	(
		city		TEXT,
		lat	 	FLOAT (8),
		lng		FLOAT (8),
		eta		INTEGER,
		time		TIMESTAMP WITH TIME ZONE NOT NULL,
		holiday		BOOLEAN,
		PRIMARY KEY (lat, lng, time)
	);""")
print "Created table 'lyft' successfully!\n"

conn.commit()

cur.close()
conn.close()
