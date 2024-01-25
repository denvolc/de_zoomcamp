import psycopg2
import os
from dotenv import load_dotenv

CREATE_TRIP_TABLE = """CREATE TABLE IF NOT EXISTS taxi_trip (
    "VendorID" BIGINT, 
	lpep_pickup_datetime TIMESTAMP WITHOUT TIME ZONE, 
	lpep_dropoff_datetime TIMESTAMP WITHOUT TIME ZONE, 
    store_and_fwd_flag TEXT, 
	"RatecodeID" BIGINT,  
	"PULocationID" BIGINT, 
	"DOLocationID" BIGINT,
    passenger_count BIGINT,
    trip_distance FLOAT(53),  
	fare_amount FLOAT(53), 
	extra FLOAT(53), 
	mta_tax FLOAT(53), 
	tip_amount FLOAT(53), 
	tolls_amount FLOAT(53),
    ehail_fee FLOAT(53),
	improvement_surcharge FLOAT(53), 
	total_amount FLOAT(53),
    payment_type BIGINT,
    trip_type BIGINT,
	congestion_surcharge FLOAT(53)
);"""

CREATE_ZONE_TABLE = """CREATE TABLE IF NOT EXISTS taxi_zones (
    "LocationID" BIGINT,
    "Borough" TEXT,
    "Zone" TEXT,
    service_zone TEXT
);"""

list_of_tables = [CREATE_TRIP_TABLE, CREATE_ZONE_TABLE]

load_dotenv()

connection = psycopg2.connect(
    database = os.environ['DATABASE'],
    user = os.environ['DATABASE_USER'],
    password = os.environ['DATABASE_PASSWORD'],
    host = os.environ['DATABASE_HOST'],
    port = os.environ['DATABASE_PORT']
)

def main():
    with connection:
        with connection.cursor() as cursor:
            for table in list_of_tables:
                cursor.execute(table)

if __name__ == '__main__':
    main()