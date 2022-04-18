#!venv\Scripts\python.exe
# -*- coding: UTF-8 -*-

####################################
#   Обробка запросів від клієнта   #
####################################

from flask import Flask, jsonify, request

from getting.get_data import json_data

app = Flask(__name__)

client = app.test_client()


# http://127.0.0.1:5000/all_accounts
@app.route('/all_accounts', methods=['GET'])
def get_list():
    json_datas = json_data()
    return jsonify(json_datas)


# from app import app, client
# r = client.post('/run_accounts', json={'login': 'password'})    |    http://127.0.0.1:5000/run_accounts
@app.route('/run_accounts', methods=['POST'])
def update_list():
    the_data_obtained = request.json
    print('Сервер отримав: ', the_data_obtained)

    return jsonify(the_data_obtained)


if __name__ == '__main__':
    app.run()
