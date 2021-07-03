from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        "Contact": "8461003827",
        "Name":"Bryan",
        "done":False,
        "id":1
    },
    {
        "Contact": "8465991773",
        "Name":"Raju",
        "done":False,
        "id":2
    }
]

@app.route("/add-data", methods = ["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please revise the data"
        },400)

    task = {
        'id':contacts[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact',""),
        'done':False
    }

    contacts.append(task)

    return jsonify({
        "status":"success",
        "message":"Task added successfully"
    })

@app.route("/get-data")

def get_task():
    return jsonify({
        "data": contacts

    })

if __name__ == '__main__':
    app.run(debug = True)