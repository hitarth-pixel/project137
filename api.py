from class2 import data1
from flask import Flask,request,jsonify
app=Flask(__name__)
@app.route('/')
def index():
    return jsonify({
        "data":data1,
        "message":"success"
    }),200
@app.route('/starData')
def specifying():
    name=request.args.get("name")
    star_data=next(item for item in data1 if item["name"]==name)
    return jsonify({
        "data":star_data,
        "message":"success",

    }),200
if __name__=="__main__":
    app.run()