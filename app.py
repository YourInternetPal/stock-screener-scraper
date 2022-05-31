from flask import Flask, request, jsonify
from flask_cors import CORS
from stockscreener import StockScreener
from settings import *

app = Flask(__name__)
CORS(app)
f = StockScreener()


@app.route("/data", methods=['GET'])
def get_from_stockscreener():
    resp = {'message': '', 'data': ''}
    ticker = request.args.get('ticker')

    # print(request.environ)
    if ticker != '':
        data = f.get_data(ticker, REQUIRED_DATA)
        if data:
            resp['message'] = "success"
            resp['data'] = data
        else:
            resp['message'] = 'failed'
    else:
        resp['message'] = 'failed'

    return jsonify(resp)


if __name__ == "__main__":
    app.run()