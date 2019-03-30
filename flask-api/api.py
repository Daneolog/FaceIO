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
default_pfp = "https://3.bp.blogspot.com/-qDc5kIFIhb8/UoJEpGN9DmI/AAAAAAABl1s/BfP6FcBY1R8/s1600/BlueHead.jpg"

person0 =  {
    "pfp" : pic0,
    "name" : "Dominic Decoco",
    "phonesOwned" : [{"image" : pic0, "name" : "Samsung S9"}],
    "interests" : ["Samsung", "Android"],
    "phoneNo" : "4701929374",
    "plan" : {"type" : "prepaid", "price": 50, "data" : "unlimited", "msg" : "unlimited", "calls" : "unlimited"},
    "isCustomer" : True
}

person1 =  {
    "pfp" : pic1,
    "name" : "Gabigol",
    "phonesOwned" : [{"image" : pic1, "name" : "Samsung S9"}],
    "interests" : ["Samsung", "Android"],
    "phoneNo" : "4701929374",
    "plan" : {"type" : "prepaid", "price": 50, "data" : "unlimited", "msg" : "unlimited", "calls" : "unlimited"},
    "isCustomer" : True
}
person2 =  {
    "pfp" : default_pfp,
    "name" : "Lucas Paqueta",
    "phonesOwned" : [{"image" : default_pfp, "name" : "Samsung S9"}],
    "interests" : ["Apple", "iPhone"],
    "phoneNo" : "4701929374",
    "plan" : {"type" : "prepaid", "price": 50, "data" : "unlimited", "msg" : "unlimited", "calls" : "unlimited"},
    "isCustomer" : True
}


fid2tid = {
    "fid0": "tid0",
    "fid1": "tid1",
    "fid2": None
}

tid2info = {"tid0" : person0, "tid1" : person1, "tid2" : person2} # faces : person_data
curr_fids = ["fid0", "fid1", "fid2"]
fid2pfp = {"fid0" : pic0, "fid1" : pic1, "fid2" : default_pfp}

@app.route("/customers", methods=['GET'])
def allCustomers():
    customers = {} 
    for fid in curr_fids:
        if fid2tid[fid] is None:
            customers[fid] = {"isCustomer" : False}
        else:
            customers[fid] = tid2info[fid2tid[fid]]
    return jsonify(customers)

@app.route("/customers/<string:fid>", methods=['GET', 'POST'])
def specificCustomer(fid):
    if request.method == 'GET':
        if fid2tid[fid] is None:
            return jsonify({"isCustomer" : False})
        return jsonify(tid2info[fid2tid[fid]])
    elif request.method == 'POST':
        tid2info[fid2tid[fid]] = request.args.get('data', None)
    else:
        return "405: Restricted method"

@app.route("/store/faces", methods=['GET'])
def store_faces():
    faces = {}
    for fid in curr_fids:
        if fid2tid[fid] is None:
            faces[fid] = {"pfp": default_pfp, "name": "undefined", "isCustomer": False}
        else:
            cust = tid2info[fid2tid[fid]]
            faces[fid] = {"pfp": cust["pfp"], "name": cust["name"], "isCustomer": True}
    return jsonify(faces)

@app.route("/store/faces/<fid>/assign/<tid>", methods=['GET'])
def assign_face_to_tid(fid, tid):
    if not tid2info[tid] is None: #tid in tid2info:
        fid2tid[fid] = tid
        tid2info[tid] = fid2pfp[fid]
        return jsonify(tid2info[tid]) 
    return 400

@app.route("/store/names", methods=['GET'])
def store_names():
    names = {}
    for tid in tid2info:
        names[tid] = tid2info[tid]["name"]
    return jsonify(names)

@app.route("/store/enter/<fid>/<img>", methods=['POST'])
def store_enter(fid, img):
    if (fid not in fid2tid):
        fid2tid[fid] = None
        fid2pfp[fid] = img
    if (fid not in curr_fids):
        curr_fids.append(fid)
    return jsonify(fid2tid[fid])


@app.route("/store/exit/<fid>", methods=['POST'])
def store_exit(fid):
    data = tid2info[fid2tid[fid]]
    curr_fids.remove(fid)
    return jsonify(data)      

@app.route("/customer/<tid>/<interest>", methods=['POST'])
def add_interest(tid, interest):
    if (tid in tid2info):
        tid2info[tid]["interests"].append(interest)
        return jsonify(tid2info[tid])

if __name__ == "__main__":
    app.run(host='0.0.0.0')
