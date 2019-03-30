import cv2
import requests
import json
import base64
import numpy as np

cap = cv2.VideoCapture(0)
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

def sendImage(image):
    subscription_key = '87d9518f24ca4658a98b2ad80dc2fb57'

    face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/identify'
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': subscription_key
    }
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        # 'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
        'returnFaceAttributes': 'age',
    }

    retval, buffer = cv2.imencode('.jpg', image)
    buffer = np.array(buffer).reshape((len(buffer)))

    #response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})
    response = requests.post(face_api_url, params=params, headers=headers, data=bytes(buffer.tolist()))
    print(json.dumps(response.json()))

currImagesCenters = []

while(True):
    # Capture frame-by-frame
    ret, image = cap.read()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        #flags = cv2.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    if len(faces) > 0:
        # for (x, y, w, h) in faces:
        #     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow("Faces found", image)
        sendImage(image)
        cap.release()
        cv2.waitKey()
        break

    cv2.imshow("Faces found", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
