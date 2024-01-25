FROM python:3.11

RUN apt-get install wget
RUN pip install pandas
RUN pip install psycopg2
RUN pip install python-dotenv

WORKDIR /app
COPY data_ingestion.py data_ingestion.py
COPY database.py database.py

ENTRYPOINT [ "python", "database.py", "data_ingestion.py"]