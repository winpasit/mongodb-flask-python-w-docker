import time
from pymongo import MongoClient
from flask import Flask
app = Flask(__name__)

client = MongoClient('mongodb://root:password@mongo:27017/') 

dblist = client.list_database_names()
if "mydatabase" not in dblist:
	mydb = client["mydatabase"]
	refresh_log = mydb["refresh_log"]
	refresh_log.insert_one({"refresh_time":0,"timestamp":time.ctime(time.time())})
	count = 0
else:
	mydb = client.mydatabase
	refresh_log = mydb["refresh_log"]
	count = refresh_log.find_one(sort=[("refresh_time", -1)])["refresh_time"]

def git_hit_count_time():
	retries = 5
	while True:
		try:
			count = refresh_log.find_one(sort=[("refresh_time", -1)])["refresh_time"]
			refresh_log.insert_one({"refresh_time":count+1,"timestamp":time.ctime(time.time())})
			result = []
			for log in refresh_log.find():
				if log['refresh_time']!= 0:
					new_log = "refresh#: "+str(log['refresh_time'])+" / timestamp: "+str(log['timestamp'])
					result.append(new_log)
			return result
		except pymongo.errors.ConnectionFailure as exc:
			if retries == 0:
				raise exc
			retries -= 1
			time.sleep(0.5)
	

@app.route('/')
def hello():
	log = git_hit_count_time()

	return str(log)