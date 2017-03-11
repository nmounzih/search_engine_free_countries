import psycopg2
import csv


conn = psycopg2.connect("dbname=search_engine_project user=nadiamounzih host=/tmp/")

cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS country (id serial PRIMARY KEY, name varchar, capital varchar, population varchar, aggregate varchar, status varchar, language varchar, export varchar);")

country_list = []
with open("country_data.csv", 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        country_list.append(row)

for data_line in country_list:
    cur.execute("INSERT INTO country (name, capital, population, aggregate, status, language, export) VALUES (%s, %s, %s, %s, %s, %s, %s)", (data_line[0], data_line[1], data_line[2], data_line[3], data_line[4], data_line[5], data_line[6]))

cur.execute("SELECT * FROM country;")
cur.fetchone()

conn.commit()

cur.close()

conn.close()
