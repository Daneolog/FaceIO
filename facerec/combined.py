import cv2
import requests
import json
import base64
import numpy as np
import time

cap = cv2.VideoCapture(0)
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
subscription_key = '87d9518f24ca4658a98b2ad80dc2fb57'

def sendimage(image):
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

def getoriginal(fid):
    face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/findsimilars'
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key
    }

    naka = "dffe3237-6f58-4ac4-9f56-bb721e8e5c6e"
    # naka2 = "cbf7e6b9-09a5-4487-9367-0b97df347a1f"
    # naka3 = "31d41da4-c51f-4c8c-8924-37198c01732c"
    mininaka = "c96c87fe-b972-4d2b-9a22-0573f9813aa7"
    mati = "fe8d6f0e-9764-4252-bc98-4249b2fde691"
    # mati2 = "2eef640d-1991-4926-b077-4f1bf2f4d8d5"
    enoch = "b2e2332e-90c7-462d-94e3-5348df491bf7"

    response = requests.post(face_api_url, headers=headers, json={
        "faceId": fid,
        "faceIds": [mati, naka, mininaka, enoch],
        # "mode": "matchFace"
    })
    response = response.json()
    if len(response) == 0 or response[0]["confidence"] < 0.7:
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

while(True):
    # Capture frame-by-frame
    ret, image = cap.read()
    cv2.imshow("FaceIO", image)
    cv2.waitKey(1)

    faces = findfaces(image)

    # Draw a rectangle around the faces
    if len(faces) > 0 and time.time() - last_sent > 4:
        # for (x, y, w, h) in faces:
        #     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        loop_time = time.time()
        while time.time() - loop_time < 1:
            ret, image = cap.read()
            cv2.imshow("FaceIO", image)
            cv2.waitKey(1)
        if len(findfaces(image)) == 0:
            continue
        fid = sendimage(image)
        if fid is None:
            last_time = time.time() - 4
            continue
        orig, confidence = getoriginal(fid)
        print(orig, confidence)
        last_time = time.time()
cap.release()
