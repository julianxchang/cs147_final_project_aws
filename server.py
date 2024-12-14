from flask import Flask, render_template
from flask import request
import csv
import os

app = Flask(__name__)

@app.route("/")
def hello():
    args = request.args.get('var')
    if args[:3] == "csv":
        if not os.path.exists("data.csv") or os.stat("data.csv").st_size == 0:
            with open("data.csv", 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Time", "Noise"])
                writer.writerow([args[3:11], args[11:-2], args[-1]])
        else:
            with open("data.csv", 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([args[3:11], args[11:-2], args[-1]])
        return "UPDATED CSV"
    else:
        labels = []
        data = []
        critical = []
        with open("data.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)
            for row in reader:
                labels.append(row[0])
                data.append(int(row[1]))
                critical.append(int(row[2]))
        return render_template("graph.html", labels=labels, data=data, critical=critical)
