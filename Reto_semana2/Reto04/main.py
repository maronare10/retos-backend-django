from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'departamentosdb'

mysql = MySQL()
mysql.init_app(app)


@app.route("/")
def index():

    # lista = ["Lima", "Lambayeque", "La libertad", "Arequipa", "Cusco", "Piura", "Tumbes", "Tacna"]
 
    cursor = mysql.get_db().cursor()

    cursor.execute('select * from departamentos')

    data = cursor.fetchall()

    cursor.close()

    print(data)

    context = {

      "ok": True,

      "content": data,

      "message": "Lista de departamentos"

    }

    return jsonify(context)
    

    # return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)