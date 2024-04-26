import requests

'''
This file is used to test the webhook

This is not a 'real' test, but a test to see if the webhook works
'''

url = "http://127.0.0.1:5000/webhook"
test_name = "NAME_HERE"
test_id = 1  # int ID

headers = {"accept": "application/json", "ID": test_id, "name": test_name}

r = requests.post(url, json=headers)
