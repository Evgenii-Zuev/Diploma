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
cursor.close()
