import urllib.request
link = urllib.request.urlopen('https://itunes.apple.com/search?term=The+Beatles')

lines = ""
for line in link.readlines():
  lines = lines + str(line)
link.close()

result = []
result = lines.split("}")

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
    print(outt.replace('}\n', '').rstrip(','))
    fl=0
  outt=""
#
# требуется из последнего принта получить массив
# массив читать, как csv_file и 
# положить его построчно в БД
#
import mysql.connector
from mysql.connector import MySQLConnection, Error
import csv
mydb = mysql.connector.connect(host='localhost',
    user='********************************',
    passwd='**********************************',
    db='******************test')
cursor = mydb.cursor()
with open('out.txt') as csv_file:   
  csv_reader = csv.reader(csv_file, delimiter=',')
  query = ("INSERT INTO the_beatles "
      "(kind,collectionName,trackName,collectionPrice,trackPrice,primaryGenreName,trackCount,trackNumber,releaseDate) "
      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
  for data in csv_reader:
######      print(data)
      cursor.execute(query, data)
############close the connection to the database.
mydb.commit()
cursor.close()
