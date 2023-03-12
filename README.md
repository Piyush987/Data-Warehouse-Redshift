# Data-Warehouse-Redshift
Build an ETL pipeline that extracts data from s3, stages in redshift and transforms data into set of dimensional tables for further analytics and insights.

## Project structure

This project includes four script files:

    create_table.py is where fact and dimension tables for the star schema in Redshift are created.
    etl.py is where data gets loaded from S3 into staging tables on Redshift and then processed into the analytics tables on Redshift.
    sql_queries.py where SQL statements are defined, which are then used by etl.py, create_table.py and analytics.py.
    dwh.cfg has config details of AWS credentials
    README.md is current file.
    
## Database schema design
Staging Tables

    staging_events
    staging_songs

Fact Table

    songplays - records in event data associated with song plays i.e. records with page NextSong - songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

Dimension Tables

    users - users in the app - user_id, first_name, last_name, gender, level
    songs - songs in music database - song_id, title, artist_id, year, duration
    artists - artists in music database - artist_id, name, location, lattitude, longitude
    time - timestamps of records in songplays broken down into specific units - start_time, hour, day, week, month, year, weekday


## Redshift
- Launch a Redshift cluster and create an IAM role that has read access to S3.
- Add redshift database and IAM role info to dwh.cfg.
- Implement the logic in etl.py to load data from S3 to staging tables on Redshift.
- Implement the logic in etl.py to load data from staging tables to analytics tables on Redshift.
- Test by running etl.py after running create_tables.py and running the analytic queries on your Redshift database to compare your results with the expected results.
