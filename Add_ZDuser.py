
from sqlite3 import Time
from urllib.request import Request


import time
import requests
#define the new user
name = "Bob Marley"
useremail = "bob.marley@strongmind.com"
verified = "true"

user = []
user.append(
    {
        'name': name,
        'email': useremail,
        'verified': verified
    }
)

# prepare the API requests
auth = 'myemail', 'mypassword'
headers = {'Content-Type': 'application/json'}
url = 'https://smtechhelp.zendesk.com/api/v2/users.json'

# post the request to Zendesk
data = {'user'}
response = requests.post(url, json=data, auth=auth, headers=headers)
if response.status_code != 200:
    print(f'Import failed with status {response.status_code}')
    exit()
print('\nImport done.')
