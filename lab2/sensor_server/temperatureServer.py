from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.dates as mdates
import io
from flask import Flask, render_template, request, send_file, make_response, redirect, url_for
import sqlite3
import sys
import datetime
import paho.mqtt.client as mqtt

dbname='sensorsData.db'
app = Flask(__name__)


# function to insert data in a table
def addData (temp):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO temperature VALUES(datetime('now'), (?))", (temp,))
    conn.commit()
    conn.close()

# print all database content
def displayAllDatabaseData():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    print ("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM temperature"):
        print (row)
    conn.close()

# get last stored data
def getLastData():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    for row in curs.execute("SELECT * FROM temperature ORDER BY timestamp DESC LIMIT 1"):
	    time = str(row[0])
	    temp = row[1]
    conn.close()
    return time, temp

def getHistData(numOfSamples):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("SELECT * FROM temperature ORDER BY timestamp DESC LIMIT " + str(numSamples))
    data = curs.fetchall()
    conn.close()
    dates = []
    temps = []
    for row in reversed(data):
	    dates.append(row[0])
	    temps.append(row[1])
    return dates, temps

@app.route("/")
def index():
    time, temp = getLastData()
    templateData = {
	    'time': time,
	    'temp': temp,
        'numSamples'	: numSamples
    }
    return render_template('index.html', **templateData)
    
@app.route('/', methods=['POST'])
def my_form_post():
    global numSamples
    numSamples = int (request.form['numSamples'])
    numMaxSamples = maxRowsTable()
    if (numSamples > numMaxSamples):
        numSamples = (numMaxSamples-1)
    time, temp = getLastData()
    templateData = {
	  	'time'	: time,
        'temp'	: temp,
        'numSamples'	: numSamples
	}
    return render_template('index.html', **templateData)


@app.route('/plot/temp')
def plot_temp():
    times, temps = getHistData(numSamples)
    ys = temps
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("Temperature [°C]")
    axis.set_xlabel("Samples")
    axis.grid(True)
    xs = range(numSamples)
    axis.plot(xs, ys)
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response

def maxRowsTable():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    for row in curs.execute("SELECT COUNT(temp) from  temperature"):
	    maxNumberRows=row[0]
    conn.close()
    return maxNumberRows

global freqSamples
global numSamples
numSamples = maxRowsTable()
if (numSamples > 101):
    numSamples = 100


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("gregor.kersevan@gmail.com/test")

def on_message(client, userdata, msg):
    message=msg.payload.decode('utf-8')
    print(msg.topic+" "+message)
    if (message != 'test maqiatto.com!'):
        addData(message)

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("maqiatto.com", 1883, 60)
    client.username_pw_set("gregor.kersevan@gmail.com", "srsisrsi")
    client.loop_start()
    # client.loop_forever()
    app.run(host='0.0.0.0', port=8080, debug=False)