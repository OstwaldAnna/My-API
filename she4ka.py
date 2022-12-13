from flask import Flask, jsonify, request
from query import Query

app = Flask(__name__)
query = Query()

@app.route("/user",methods = ['GET'])
def get_user():
    try:
        data = []
        query_data = query.get_user()
        if type(query_data) == list:
            for item in query_data:
                data.append(item.as_dict())
            return jsonify(data), 200
        else:
            return jsonify({"message":"Error in request"}), 400
    except Exception as ex:
       return jsonify({"message":str(ex)}), 400

if __name__ == '__main__':
    app.run(debug=True )