import requests

url = "http://localhost:1552/predict"
customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 10}
resp = requests.post(url, json=customer).json()
print(resp)
