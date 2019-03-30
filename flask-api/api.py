from flask import Flask, jsonify, request
import flask
import json
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()

app = Flask(__name__)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    return response
pic0 = "https://scontent-atl3-1.xx.fbcdn.net/v/t31.0-8/1926287_542834289163885_1403268875_o.jpg?_nc_cat=106&_nc_ht=scontent-atl3-1.xx&oh=a87047ab6817fe144e3e819b311b5d31&oe=5D4EB408"
pic1 = "https://media.licdn.com/dms/image/C5603AQG6BF4IsM7Eaw/profile-displayphoto-shrink_200_200/0?e=1559174400&v=beta&t=H0VDKP5cQA4zf-gdFLIhuOoNf2ANBi3AKCBF2JG2i-o"
person0 =  {
                "pfp" : "oi",
                "name" : "Dominic Decoco",
                "phonesOwned" : [{"image" : pic0, "name" : "Samsung S9"}],
                "interests" : ["Samsung", "Android"],
                "phoneNo" : "4701929374",
                "plan" : {"type" : "prepaid", "price": 50, "data" : "unlimited", "msg" : "unlimited", "calls" : "unlimited"}
            }
            

person1 =  {
                "pfp" : "oi",
                "name" : "Gabigol",
                "phonesOwned" : [{"image" : pic1, "name" : "Samsung S9"}],
                "interests" : ["Samsung", "Android"],
                "phoneNo" : "4701929374",
                "plan" : {"type" : "prepaid", "price": 50, "data" : "unlimited", "msg" : "unlimited", "calls" : "unlimited"}
            }

fid2tid = {
    "fid0": "tid0",
    "fid1": "tid1",
    "fid2": None
}
tid2info = {"tid0" : person0, "tid1" : person1} # faces : person_data
curr_fids = ["fid0", "fid1"]

@app.route("/customers", methods=['GET'])
def allCustomers():
    customers = {} 
    for fid in curr_fids:
        customers[fid] = tid2info[fid2tid[fid]]
    return jsonify(customers)

@app.route("/customers/<key>", methods=['GET', 'POST'])
def specificCustomer(key):
    if request.method == 'GET':
        if tid2info[fid] is None:
            return jsonify({})
        return jsonify(tid2info[fid2tid[key]])
    elif request.method == 'POST':
        tid2info[fid2tid[key]] = request.args.get('data', None)
    else:
        return "405: Restricted method"

@app.route("/store/faces", methods=['GET'])
def store_faces():
    faces = {}
    for fid in curr_fids:
        if fid2tid[fid] is None:
            faces[fid] = {"pfp": "", "name": "undefined", "isCustomer": False}
        else:
            cust = tid2info[fid2tid[fid]]
            faces[fid] = {"pfp": cust["pfp"], "name": cust["name"], "isCustomer": True}
    return jsonify(faces)

@app.route("/store/faces/<fid>/assign/<tid>", methods=['GET'])
def assign_face_to_tid(fid, tid):
    if tid in tid2info:
        fid2tid[key] = tid
        return 200
    return 400

if __name__ == "__main__":
    app.run(host='0.0.0.0')
