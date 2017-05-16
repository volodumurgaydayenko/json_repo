import shelve
from flask import Flask

with shelve.open('shelve.db') as db:
    db['_meta'] = {'filename': 'shelve.db'}

with shelve.open('shelve.db') as db:
    print(db['_meta'])

app = Flask(__name__)

# dbname =


@app.route('/db/get', methods=['GET'])
def get_db():
    return


if __name__ == '__main__':
    print('server_db', 'Vova', 'q1q2w3r4')
    app.run(debug=False)
