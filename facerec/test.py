import requests
import json

subscription_key = '87d9518f24ca4658a98b2ad80dc2fb57'
assert subscription_key

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'

image_url = 'https://media.licdn.com/dms/image/C5603AQG6BF4IsM7Eaw/profile-displayphoto-shrink_200_200/0?e=1559174400&v=beta&t=H0VDKP5cQA4zf-gdFLIhuOoNf2ANBi3AKCBF2JG2i-o'

headers = { 'Ocp-Apim-Subscription-Key': subscription_key }
    
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

data = open("/Users/GabrielNAN/Desktop/gabri.jpeg", "rb")

#response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})
response = requests.post(face_api_url, params=params, headers=headers, data=data)
print(json.dumps(response.json()))
