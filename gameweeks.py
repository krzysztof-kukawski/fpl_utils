import requests
import json

data = requests.get('https://fantasy.premierleague.com/api/event/19/live/')
data = json.loads(data.content)

print(data.keys())
print(data)