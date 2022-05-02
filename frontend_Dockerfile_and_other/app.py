from flask import Flask, render_template
import os
import MySQLdb
from prometheus_flask_exporter import PrometheusMetrics
import requests
from dotenv import load_dotenv

app = Flask(__name__)

#metrics = PrometheusMetrics(app)
load_dotenv('.env')

def connection():
    conn = MySQLdb.connect(host=os.getenv('mysql_host'),
                           user=os.getenv('mysql_user'),
                           password=os.getenv('mysql_password'),
                           database=os.getenv('mysql_db'),
                           charset='utf8')
    c = conn.cursor()
    return c, conn

@app.route('/')
def index():
    try:
        c, conn = connection()
        query = "select kind, collectionName, trackName, collectionPrice, \
                 trackPrice, primaryGenreName, trackCount, trackNumber, \
                 releaseDate from the_beatles \
                 order by collectionName, releaseDate"
        c.execute(query)
        data = c.fetchall()
        conn.close()
        return render_template("index.html", data=data)
        return data
    except Exception as e:
        return (str(e))

