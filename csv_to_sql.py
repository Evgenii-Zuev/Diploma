import mysql.connector
from mysql.connector import MySQLConnection, Error
import csv
mydb = mysql.connector.connect(host='localhost',
    user='<***>',
    passwd='<***>',
    db='test')
cursor = mydb.cursor()
with open('out.txt') as csv_file:   
  csv_reader = csv.reader(csv_file, delimiter=',')
  query = ("INSERT INTO the_beatles "
      "(kind,collectionName,trackName,collectionPrice,trackPrice,primaryGenreName,trackCount,trackNumber,releaseDate) "
      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
  for data in csv_reader:
#      print(data)
      cursor.execute(query, data)
#####close the connection to the database.
mydb.commit()
cursor.close()
print("Done")
