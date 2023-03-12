import psycopg2
import configparser

config = configparser.ConfigParser()
config.read('dwh.cfg')

# Set up a connection to Redshift
conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))

# Create a cursor object
cur = conn.cursor()

# Execute a SELECT query
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_name;")

# Fetch the results
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()