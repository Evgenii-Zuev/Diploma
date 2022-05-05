import requests
#from datetime import datetime, timedelta
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from prometheus_flask_exporter import PrometheusMetrics
import os

def refresh():
   import urllib.request
   link = urllib.request.urlopen('https://itunes.apple.com/search?term=The+Beatles')

   lines = ""
   for line in link.readlines():
     lines = lines + str(line)
   link.close()

   result = []
   result = lines.split("}")
   file = open(r"out.txt", "w")

   substr = ['kind','collectionName', 'trackName', 'collectionPrice', 'trackPrice', 'primaryGenreName', 'trackCount', 'trackNumber', 'releaseDate']
   outt=""
   fl=0
   for text0 in result:
     i=0
     while i<len(substr):
       b=text0.find(substr[i])
       if b == -1:
         outt=outt+" ,"
       else:
         if substr[i] == "releaseDate":
           outt=outt+(text0[b+len(substr[i])+2:]).split(',')[0].replace('T', ' ').replace('Z', '').replace('"', '')+","
         else:
           outt=outt+(text0[b+len(substr[i])+2:]).split(',')[0].replace('"', '')+","
         fl+=1
       i+=1
     if fl>0:
       file.write(outt.replace('}\n', '').rstrip(',')+'\n')
       fl=0
     outt=""
   file.close()

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

   with open('out.txt') as csv_file:
     csv_reader = csv.reader(csv_file, delimiter=',')
     query = ("INSERT INTO the_beatles "
         "(kind,collectionName,trackName,collectionPrice,trackPrice,primaryGenreName,trackCount,trackNumber,releaseDate) "
         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
     for data in csv_reader:
         cursor.execute(query, data)
   mydb.commit()
   cursor.close()
   csv_file.close()
   os.remove('out.txt')

@app.route('/refresh', methods=['GET'])
def get_tasks():
    refresh()
    return "ok"

@app.route('/healthz')
def healthz():
    return "OK"
