from flask import Flask
from replit import db

db.get('views', {})
app = Flask('app')
a=0
@app.route('/')
def hello_world():
	global a
	a+=1
	db["views"] = a
	return 'Hello, World!'+str(db['views'])


app.run(host='0.0.0.0', port=8080)