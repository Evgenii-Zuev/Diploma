#!/usr/bin/env python
# требуется очистить таблицу перед занесением данных
import os
from dotenv import load_dotenv
load_dotenv('.env')
import mysql.connector
from mysql.connector import MySQLConnection, Error
import csv
mydb = mysql.connector.connect(host=os.getenv('mysql_host'),
    user=os.getenv('mysql_user'),
    passwd=os.getenv('mysql_password'),
    db=os.getenv('mysql_db'))

cursor = mydb.cursor()
query = ("DELETE FROM the_beatles")
cursor.execute(query)
mydb.commit()

with open('out_old.txt') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  query = ("INSERT INTO the_beatles "
      "(kind,collectionName,trackName,collectionPrice,trackPrice,primaryGenreName,trackCount,trackNumber,releaseDate) "
      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
  for data in csv_reader:
#######      print(data)
      cursor.execute(query, data)
###########close the connection to the database.
mydb.commit()
cursor.close()
csv_file.close()
#os.remove('out.txt')

