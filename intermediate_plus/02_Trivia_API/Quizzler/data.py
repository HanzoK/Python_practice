import requests

parameters = {
    "amount": 10,
    "type": "boolean"
    # Change the number below to change category for the quiz. 18 = Computer-science related questions
    # "category": 18,
}

response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]