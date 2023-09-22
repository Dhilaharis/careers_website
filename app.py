from flask import Flask ,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
# from flask_mysqldb import MySQL


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:ok@localhost/alchamy'
db = SQLAlchemy(app)
# app.config["MYSQL_HOST"]="localhost"
# app.config["MYSQL_USER"]="root"
# app.config["MYSQL_PASSWORD"]="mysql11"
# app.config["MYSQL_DB"]="career"
# app.config["MYSQL_CURSORCLASS"]="Dictcursor"
# mysql=MySQL(app)

Jobs=[{
  'role':'Data science',
  'exp':'2yrs',
  'location':'Chennai'
},{
  'role':'Data analyst',
  'exp':'1yrs',
  'location':'Coimbatore'
}]

@app.route('/')
def index():
  # con=mysql.connection.cursor()
  # sql="INSERT into employees(title) value ('Data')"
  # con.execute(sql)
  # mysql.connection.commit()
  return render_template("home.html",jobs=Jobs)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(Jobs)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)