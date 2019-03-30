from flask import Flask, jsonify, request
import flask
import json
import socket
from sendemail import send_email
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
mati = "fe8d6f0e-9764-4252-bc98-4249b2fde691"
gabri = "93e75fce-0273-483f-bfd8-4b9d32df9aec"
alicia = "d818339e-ecfd-45ed-b11c-889546308693"
p3 = "b2e2332e-90c7-462d-94e3-5348df491bf7"
s9 = "https://images-na.ssl-images-amazon.com/images/I/81wLkQ64HXL._SX522_.jpg"
iPhone = "https://images-na.ssl-images-amazon.com/images/I/51dYN7VDKWL.jpg"
promo1 = "https://www.t-mobile.com/content/dam/t-mobile/deals/background-images/240226_Q1_Plans-Plus-Affordable.desktop.jpg"
promo2 = "https://d1ic4altzx8ueg.cloudfront.net/finder-us/wp-uploads/2017/08/get-deal.jpeg"
promo3 = "https://www.androidguys.com/wp-content/uploads/2017/10/T-Mobile-BYOD-Google-Pixel-2-promo.png"
pixel2 = "https://img1.ibay.com.mv/is1/full/2018/07/item_2280938_357.jpg"



person0 =  {
    "pfp" : pic0,
    "name" : "Davi N. A.",
    "phonesOwned" : [{"img" : s9, "name" : "Samsung S9"}],
    "interests" : ["OnePlus", "Android", "couple"],
    "phoneNo" : "4701466375",
    "plan" : {"type" : "prepaid", "price": 50, "data" : "unlimited", "msg" : "unlimited", "calls" : "unlimited"},
    "age" : 19,
    "gender": "male",
    "isCustomer" : True,
    "email": "davi.nakajima.an@gmail.com"
}

person1 =  {
    "pfp" : pic1,
    "name" : "Gabriel N. An",
    "phonesOwned" : [{"img" : s9, "name" : "Samsung S9"}, {"img" : iPhone, "name" : "iPhone 6"}],
    "interests" : ["Samsung", "Android", "couple"],
    "phoneNo" : "4701929384",
    "plan" : {"type" : "prepaid", "price": 50, "data" : "unlimited", "msg" : "unlimited", "calls" : "unlimited"},
    "age" : 22,
    "gender": "male",
    "isCustomer" : True,
    "email": "gabriel.nakajima.an@gmail.com"
}

person2 =  {
    "pfp" : default_pfp,
    "name" : "Mati S.",
    "phonesOwned" : [{"img":pixel2,"name" : "Pixel 2"}],
    "interests" : ["Apple", "iPhone", "Pixel"],
    "phoneNo" : "4043126300",
    "plan" : {"type" : "prepaid", "price": 50, "data" : "unlimited", "msg" : "unlimited", "calls" : "unlimited"},
    "age" : 21,
    "gender": "male",
    "isCustomer" : True,
    "email": "mszylkowski@hotmail.com"
}

person3 =  {
    "pfp" : default_pfp,
    "name" : "Enoch K.",
    "phonesOwned" : [{"img": iPhone ,"name" : "iPhone 6"}],
    "interests" : ["Apple", "iPhone"],
    "phoneNo" : "4046426209",
    "plan" : {"type" : "prepaid", "price": 50, "data" : "unlimited", "msg" : "unlimited", "calls" : "unlimited"},
    "age" : 24,
    "gender": "male",
    "isCustomer" : True,
    "email": "daneolog@gmail.com"
}
promotion =  {
    "promo1" : {"icon" : promo1, "description" : "Phones included w/ unlimited 2 phones + 2 lines for $100","qualified" : [person1, person0]},
    "promo2" : {"icon" : promo2, "description" : "Samsung Galaxy S10 for under $700","qualified" : [person0]},
    "promo3" : {"icon" : promo3, "description" : "Bring your Pixel 2 to T-Mobile and get 50% back", "qualified" : [person2]}
}
fid2tid = {
    # mati: "tid0",
    # gabri: "tid1",
    p3 : None
}

interests = {}#{mati: [], gabri: [], p3: []}

tid2info = {"tid0": person0, "tid1": person1, "tid2" : person2}#, "tid2" : person2} # faces : person_data
curr_fids = [p3]
# fid2pfp = {mati : pic0, gabri : pic1,  p3 : default_pfp}
fid2profile = {
    #mati : {"pfp" : pic0, "age": 21, "gender": "male"},
    # gabri : {"pfp" : pic1, "age": 22, "gender": "male"},
    p3 : {"pfp" : pic0, "age": 24, "gender": "male"}
}

fids_visited = []

@app.route("/customers", methods=['GET'])
def allCustomers():
    # customers = [] 
    # for fid in fid2tid:
    #     if fid2tid[fid] is None:
    #         customers[fid] = {"isCustomer" : False, "pfp" : fid2profile[fid]["pfp"]}
    #     else:
    #         customers[fid] = tid2info[fid2tid[fid]]
    return jsonify(fid2tid.keys())


@app.route("/customers/<string:fid>", methods=['GET'])
def specificCustomer(fid): # mark visited
    if fid not in fids_visited:
        fids_visited.append(fid)
    if fid2tid[fid] is None:
        return jsonify({"isCustomer" : False})
    return jsonify(tid2info[fid2tid[fid]])
    
@app.route("/promotions", methods=['GET'])
def promotions(): 
    return jsonify(promotion)

@app.route("/store/faces", methods=['GET'])
def store_faces():
    print curr_fids
    faces = {}
    for fid in curr_fids:
        if fid2tid[fid] is None:
            faces[fid] = {"wasAttended": fid in fids_visited, "pfp": fid2profile[fid]["pfp"], "name": "undefined", "isCustomer": False, "age" : fid2profile[fid]["age"], "gender" : fid2profile[fid]["gender"]}
        elif (fid in fid2tid):
            cust = tid2info[fid2tid[fid]]
            faces[fid] = {"wasAttended": fid in fids_visited, "pfp": cust["pfp"], "name": cust["name"], "age": cust["age"], "gender": cust["gender"], "isCustomer": True}
    return jsonify(faces)

@app.route("/store/faces/<fid>/assign/<tid>", methods=['GET'])
def assign_face_to_tid(fid, tid):
    if not tid2info[tid] is None: #tid in tid2info:
        fid2tid[fid] = tid
        tid2info[tid]["pfp"] = fid2profile[fid]["pfp"]
        return jsonify(tid2info[tid]) 
    return 400

@app.route("/store/names", methods=['GET'])
def store_names():
    names = {}
    for tid in tid2info:
        names[tid] = tid2info[tid]["name"]
    return jsonify(names)

@app.route("/store/enter/<string:fid>", methods=['POST'])
def store_enter(fid):
    if (fid not in fid2tid):
        fid2tid[fid] = None
        data = request.get_json()

        print data["imgUrl"] # request.args.get("imgUrl")

        fid2profile[fid] = {
            "pfp" : data['imgUrl'],
            "age" : data['age'],
            "gender" : data['gender']
        }
    if (fid not in curr_fids):
        curr_fids.append(fid)
    return jsonify(fid2tid[fid])


@app.route("/store/exit/<string:fid>", methods=['POST'])
def store_exit(fid):
    print "--------------------------------"
    if fid in curr_fids:
        # data = tid2info[fid2tid[fid]]
        data = []
        if fid in interests:
            data = interests[fid]
            del interests[fid]
            send_email(tid2info[fid2tid[fid]]["email"], data)
        if fid in fids_visited:
            fids_visited.remove(fid)
        curr_fids.remove(fid)
        print data
        return jsonify(data)      
    return ({})

@app.route("/customer/<fid>/<interest>", methods=['POST'])
def add_interest(fid, interest):
    tid2info[fid2tid[fid]]["interests"].append(interest)
    if interest not in interests:
        interests[fid] = [interest]
    else:
        interest[fid].append(interest)
    return jsonify(tid2info[fid2tid[fid]])

@app.route("/fids", methods=['GET'])
def all_fids():
    return jsonify(curr_fids)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
