#!/usr/bin/env python

import mysql.connector
import sys
mycolor=0

myconn = mysql.connector.connect(
      host="localhost",
      user="root",
      password="GE*5if2n",
      database="test"
)
cur = myconn.cursor()

try:
    cur.execute("select * from the_beatles order by collectionName, releaseDate")

    result = cur.fetchall()
    #printing the result

    print "Content-type: text/html\n\n"
    print "<html>\n<body>\n"
    print "<div style=\"width: 100%; font-size: 14px; font-weight: bold; text-align: center;\">\n"
    print( '<table border="0">');
    print( '<thead>');
    print( '<font color="blue">');
    print( '<tr style="background-color:rgb(128, 128, 0);"</tr>');
    print( '<th><font color="white">kind</font></th>');
    print( '<th><font color="white">collectionName</font></th>');
    print( '<th><font color="white">trackName</font></th>');
    print( '<th><font color="white">collectionPrice</font></th>');
    print( '<th><font color="white">trackPrice</font></th>');
    print( '<th><font color="white">primaryGenreName</font></th>');
    print( '<th><font color="white">trackCount</font></th>');
    print( '<th><font color="white">trackNumber</font></th>');
    print( '<th><font color="white">releaseDate</font></th>');
    print( '</font>');
    print( '</tr>');
    print( '</thead>');
    print( '<tbody>');

    for x in result:
      if mycolor == 0:
        mycolor=1
        print('<tr style="background-color:rgb(255, 255, 204);"><td>'+str(x[0])+'</td><td>'+str(x[1])+
              '</td><td>'+str(x[2])+'</td><td>'+str(x[3])+'</td><td>'+str(x[4])+'</td><td>'+str(x[5])+
              '</td><td>'+str(x[6])+'</td><td>'+str(x[7])+'</td><td>'+str(x[8])+'</td></tr>');
      else:
        mycolor=0
        print('<tr style="background-color:rgb(204, 255, 255);"><td>'+str(x[0])+'</td><td>'+str(x[1])+
              '</td><td>'+str(x[2])+'</td><td>'+str(x[3])+'</td><td>'+str(x[4])+'</td><td>'+str(x[5])+
              '</td><td>'+str(x[6])+'</td><td>'+str(x[7])+'</td><td>'+str(x[8])+'</td></tr>');

    print('</tbody>');
    print('</table>');
    print "\n</div>\n"
    print "</body>\n</html>\n"
except:
    myconn.rollback()
myconn.close()
