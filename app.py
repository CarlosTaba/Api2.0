from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) ## To allow direct AJAX calls

@app.route('/datos', methods=['GET'])
def home():
    r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=19.54&longitude=-96.91&current_weather=true')

    return r.json()

if __name__ == '__main__':
   app.run(debug = True)