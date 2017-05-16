from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/db/get', methods=['GET'])
def get_db():
    return jsonify


if __name__ == '__main__':
    print('server_db', 'Vova', 'q1q2w3r4')
    app.run(debug=False)
