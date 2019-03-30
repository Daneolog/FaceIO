import cv2
import requests
import json
import base64
import numpy as np
import time
import sys

if len(sys.argv) == 1:
    print("You need to pass in as a parameter \"enter\" or \"exit\" to determine the camera placement")
state = sys.argv[1]
if state not in ["enter", "exit"]:
    print("You need to pass in as a parameter \"enter\" or \"exit\" to determine the camera placement")
    sys.exit()

cap = cv2.VideoCapture(0)
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
subscription_key = '87d9518f24ca4658a98b2ad80dc2fb57'

# fids2names = {
#
#     "93e75fce-0273-483f-bfd8-4b9d32df9aec": "naka",
#     # "dffe3237-6f58-4ac4-9f56-bb721e8e5c6e": "naka1",
#     # "cbf7e6b9-09a5-4487-9367-0b97df347a1f": "naka2",
#     # "31d41da4-c51f-4c8c-8924-37198c01732c": "naka3",
#     "c96c87fe-b972-4d2b-9a22-0573f9813aa7": "mininaka",
#     "fe8d6f0e-9764-4252-bc98-4249b2fde691": "mati",
#     # "2eef640d-1991-4926-b077-4f1bf2f4d8d5": "mati2",
#     "b2e2332e-90c7-462d-94e3-5348df491bf7": "enoch",
# }
# fids_list = list(fids2names.keys())


all_faces = {}

if state == "enter":
    response = requests.get("http://10.136.8.228:5000/store/faces").json()
    all_faces = set(response.keys())


def getFaceId(image):
    print("Recognizing image")
    face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': subscription_key
    }
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        # 'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }

    retval, buffer = cv2.imencode('.jpg', image)
    buffer = np.array(buffer).reshape((len(buffer)))

    response = requests.post(face_api_url, params=params, headers=headers, data=bytes(buffer.tolist()))
    response = response.json()
    if len(response) == 0:
        print("No faces recognized from Azure")
        return None
    fid = response[0]["faceId"]
    return fid


def getOriginalId(fid):
    global all_faces
    face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/findsimilars'
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key
    }

    if state == "exit":
        all_faces = set(requests.get("http://10.136.8.228:5000/fids").json())

    print('List of current face ids:', all_faces)

    response = requests.post(face_api_url, headers=headers, json={
        "faceId": fid,
        "faceIds": list(all_faces),
        # "mode": "matchFace"
    })
    response = response.json()
    if type(response) != list:
        print(response)
        return fid, 0
    if len(response) == 0 or response[0]["confidence"] < 0.0:
        return fid, 0
    return response[0]["faceId"], response[0]["confidence"]


def findfaces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    return faces


last_sent = time.time()
max_blur = 0
max_blur_image = None
margin = 50
size_threshold = 15000

default_size = (50, 50)

consecutive_time = time.time()
consecutive_th = 1

send_th = 3
send_time = time.time() - send_th

while True:
    # Capture frame-by-frame
    ret, image = cap.read()

    faces = findfaces(image)
    if len(faces) > 0 and time.time() - send_time > send_th:
        faces = sorted(faces, key=lambda face: face[2]*face[3])
        (x, y, w, h) = faces[-1]
        image_size = w * h
        height, width, _ = image.shape
        face = image[max(0, y - margin):min(y + h + margin, height),
                     max(0, x - margin):min(width, x + w + margin)]

        # print(image_size)
        curr_blur = cv2.Laplacian(face, cv2.CV_64F).var()
        if image_size > size_threshold and curr_blur > max_blur:
            max_blur = curr_blur
            max_blur_image = face
            consecutive_time = time.time()
        if max_blur_image is not None:
            cv2.imshow('FaceIO', max_blur_image)
            if time.time() - consecutive_time > consecutive_th:
                fid = getFaceId(max_blur_image)
                if fid is not None:
                    original_id, confidence = getOriginalId(fid)
                    send_time = time.time()
                    if state == "exit":
                        requests.post("http://10.136.8.228:5000/store/exit/" + original_id)
                        print('Sending exit of user with face id: {}'.format(fid))
                        print()
                    else:
                        string_image = cv2.imencode('.jpg', cv2.resize(max_blur_image, default_size))[1]
                        string_image = base64.b64encode(string_image)
                        requests.post("http://10.136.8.228:5000/store/enter/" + original_id,
                                      json={"imgUrl": "data:image/jpeg;base64," + string_image.decode("utf-8"),
                                            "age": 11,
                                            "gender": 'male'})
                        all_faces.add(original_id)
                        print('Sending {} face to server'.format('NEW' if confidence == 0 else "OLD"))
                        print()
                else:
                    max_blur_image = None
                    max_blur = 0

    else:
        cv2.imshow("FaceIO", image)
        max_blur = 0
        max_blur_image = None
    cv2.waitKey(1)

    # if len(faces) > 0 and time.time() - last_sent > 4:



    # Draw a rectangle around the faces
    # if len(faces) > 0 and time.time() - last_sent > 4:
    #     # for (x, y, w, h) in faces:
    #     #     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    #     loop_time = time.time()
    #     while time.time() - loop_time < 1:
    #         ret, image = cap.read()
    #         cv2.imshow("FaceIO", image)
    #         cv2.waitKey(1)
    #     if len(findfaces(image)) == 0:
    #         continue
    #     fid = sendimage(image)
    #     if fid is None:
    #         last_sent = time.time() - 4
    #         continue
    #     orig, confidence = getoriginal(fid)
    #     print(orig, confidence)
    #     last_sent = time.time()
