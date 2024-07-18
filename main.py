import requests
from datetime import datetime

today = datetime.now()

USERNAME = "whoisthis"
TOKEN = "anything"
GRAPH_ID = "graph"
DATE = today.strftime("%Y%m%d")
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes", 
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Study Graph",
    "unit": "hour",
    "type": "float",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
#print(today.strftime("%Y%m%d"))

pixel_config = {
    "date": DATE,
    "quantity": input("How many hours did you study today? ")
}


pixel_response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(pixel_response.text)


pixel_put_endpoint = f"{pixel_endpoint}/{DATE}"

request_body = {
    "quantity": "6.0",
}

#put_response = requests.put(url=pixel_put_endpoint, json=request_body, headers=headers)
#print(put_response.text)

#delete_response = requests.delete(url=pixel_put_endpoint, headers=headers)
#print(delete_response.text)