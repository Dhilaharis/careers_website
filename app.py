from flask import Flask ,render_template,jsonify

app=Flask(__name__)

Jobs=[{
  'role':'Data science',
  'exp':'2yrs',
  'location':'chennai'
},{
  'role':'Data analyst',
  'exp':'1yrs',
  'location':'coimbatore'
}]

@app.route('/')
def index():
  return render_template("home.html",jobs=Jobs)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(Jobs)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)