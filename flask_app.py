import json
import requests
from flask import Flask, request, render_template, jsonify


app = Flask(__name__)

@app.route('/')
def index():

    country = request.args.get('country', 'Albania').capitalize()

    data = requests.get('https://pomber.github.io/covid19/timeseries.json').json()

    dates = []
    infections = []

    for day in data[country]:
        dates.append(day['date'].replace("2020-", ""))
        infections.append(day['confirmed'])

    return render_template('index.html', DATES=dates, INFECTIONS=infections, COUNTRY=country)


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
