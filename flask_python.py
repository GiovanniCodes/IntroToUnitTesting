from pymongo import MongoClient
from flask import Flask
client = MongoClient("mongodb://user:gg1234@cluster0-shard-00-00-wpaly.mongodb.net:27017,cluster0-shard-00-01-wpaly.mongodb.net:27017,cluster0-shard-00-02-wpaly.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.assign2
results = db.results
entries = db.entries
retireEntries = db.retireEntries


app = Flask(__name__)



@app.route("/distance/")
def distanceHTTP():
    pymongo_cursor = db.collection.find()
    allDistData = ''
    for document in entries.find({}, {"_id": 0, "x1": 1, "x2": 1, 'y1': 1, "y2": 1, "timestamp": 1}):
        #print(document)  # iterate the cursor
        tempRetire = str(document)
        allDistData = allDistData + tempRetire

    return allDistData

@app.route("/retirement/")
def retirementHTTP():
    pymongo_cursor = db.collection.find({})
    allRetireData = ''
    for document in retireEntries.find({}, {"_id": 0, "age": 1, "annualSalary": 1, 'percentSaved': 1,
                                            "retirementSaveGoal": 1}):
        #print(document)  # iterate the cursor
        tempRetire = str(document)
        allRetireData = allRetireData + tempRetire

    return allRetireData

if __name__ == "__main__":
    app.run()
