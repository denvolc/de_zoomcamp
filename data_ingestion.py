import pandas as pd
from dotenv import load_dotenv
import psycopg2
import os

data_path = './source/green_tripdata_2019-09.csv'
zones_path = './source/taxi+_zone_lookup.csv'
trip_table = 'taxi_trip'
zones_table = 'taxi_zones'

load_dotenv()

connection = psycopg2.connect(
    database = os.environ['DATABASE'],
    user = os.environ['DATABASE_USER'],
    password = os.environ['DATABASE_PASSWORD'],
    host = os.environ['DATABASE_HOST'],
    port = os.environ['DATABASE_PORT']
)

def copy_csv_to_postgres(source_csv, table_name):
    with connection:
        with connection.cursor() as cursor:
            with open(source_csv, 'r') as f:
                next(f)
                try:
                    cursor.copy_from(f, table_name, sep=',', null='')
                except (Exception, psycopg2.DatabaseError) as error:
                    print(f"Error: {error}")
                    connection.rollback()

def main():
    copy_csv_to_postgres(data_path, trip_table)
    copy_csv_to_postgres(zones_path, zones_table)

if __name__ == '__main__':
    main()
