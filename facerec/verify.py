import requests
import json

subscription_key = '87d9518f24ca4658a98b2ad80dc2fb57'

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/findsimilars'
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key
}

#response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})
naka1 = "dffe3237-6f58-4ac4-9f56-bb721e8e5c6e"
naka2 = "cbf7e6b9-09a5-4487-9367-0b97df347a1f"
naka3 = "31d41da4-c51f-4c8c-8924-37198c01732c"
mininaka = "c96c87fe-b972-4d2b-9a22-0573f9813aa7"
mati1 = "fe8d6f0e-9764-4252-bc98-4249b2fde691"
mati2 = "2eef640d-1991-4926-b077-4f1bf2f4d8d5"
enoch = "b2e2332e-90c7-462d-94e3-5348df491bf7"

response = requests.post(face_api_url, headers=headers, json={
    "faceId": enoch,
    "faceIds": [mati1, mati2, naka1, mininaka, naka2, naka3],
    # "mode": "matchFace"
})
print(json.dumps(response.json()))
