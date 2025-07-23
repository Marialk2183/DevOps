from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db
collection = db.todos

@app.route('/submittodoitem', methods=['POST'])
def submit_item():
    name = request.form['itemName']
    desc = request.form['itemDescription']
    collection.insert_one({"name": name, "description": desc})
    return "Item submitted!"
