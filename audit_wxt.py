import json
import requests

token = ""
room = ""

params = {
    'roomId' : room,
    'max':'1000'}
headers = {
    'Authorization': "Bearer " + token,
    'Content-Type': "application/json",
    }

req = requests.get('https://api.ciscospark.com/v1/memberships', headers=headers ,params=params)
members = json.loads(req.text)

for item in members["items"]:
	domain = item["personEmail"].split('@')[1]
	if domain == 'yahoo.com' or domain == 'hotmail.com' or domain == 'gmail.com':
		print (item["personDisplayName"] + " " + item["personEmail"])
		print ("https://api.ciscospark.com/v1/memberships/" + item["id"])
		requests.delete("https://api.ciscospark.com/v1/memberships/" + item["id"], headers=headers)
