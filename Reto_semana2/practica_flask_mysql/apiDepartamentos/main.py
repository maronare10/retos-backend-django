from flask import Flask, render_template
from flask.json import jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'listaDepartamentos'

mysql = MySQL()
mysql.init_app(app)


@app.route("/")
def index():

    title = 'BUILDINGS'

    cursor = mysql.get_db().cursor()

    cursor.execute('select*from buildings')

    data = cursor.fetchall()

    cursor.close()

    print(data)

    context = {
        'title': title,
        'data' : data

    }

    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
