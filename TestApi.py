import requests
import json

url = "http://127.0.0.1:5005/model/parse"

payload = json.dumps({
  "text": "Hello. The issue is still not resolved."
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
result=json.loads(response.text.encode('utf8'))
sentiment = result["intent"]["name"]
confidence = round(float(result["intent"]["confidence"] or '0.0')*100,2)
print("Sentiment: ",sentiment)
print("Confidence: ",confidence,"%")