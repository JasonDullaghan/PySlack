import json
import requests
from selenium import webdriver
import os
from pathlib import Path
from dotenv import load_dotenv
from decouple import config

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://youtube.com")


webhook_url = config('WEB')
slack_data = {'text': driver.title}

response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )