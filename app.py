from flask import Flask, request, jsonify
from flask.templating import render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'BusDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql.init_app(app)

conn = mysql.connect()
cursor =conn.cursor()

@app.route("/user",methods=['POST',"GET"])
def user():
    if request.method == "GET":
        cursor.execute("SELECT * from user")
        data = cursor.fetchone()
        print(data)
        return str(data)

@app.route("/bus",methods=['POST',"GET"])
def bus():
    if request.method == "GET":
        cursor.execute("SELECT * from bus")
        data = cursor.fetchone()
        print(data)
        return str(data)

@app.route("/register",methods=['POST','GET'])
def register():
    if request.method == 'POST':
        form = request.form
        name = form['name']
        age = int(form['age'])
        gender = form['gender']
        sql = f"insert into user(name,age,gender) values('{name}',{age},'{gender}')"
        # print(sql)
        cursor.execute(sql)
        conn.commit()
        return "Success"
    if request.method == 'GET':
        return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')