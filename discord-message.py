from dotenv import load_dotenv
import os
import requests
import random
import time

messages = [
    "Hello and welcome!",
    "Welcome to the server!",
    "Hey there, welcome to our community!",
    "Hai ther, welcom to the club!",
    "Hi and welcome aboard!",
    "Hey, welcome to the team!",
    "Good to see you here, welcome!",
    "Welcom, we're glad to have you!",
    "Hey there, welcom to the community!",
    "Welcom to our group, let's get started!",
    "Helo and welcom to our server!",
    "Glad to have you with us, welcome!",
    "We're thrilled you've joined, welcome!",
    "Welcome, we hope you enjoy your time here!",
    "Hey, thanks for joining us! Welcome!",
    "Welcome to our community, let us know if you have any questions!",
    "We're so happy to see you here, welcome!",
    "Hello and a warm welcome to our group!",
    "Thanks for being a part of our community, welcome!",
    "We hope you feel at home here. Welcome!",
    "what price are y'all predicting", 
    "wen mainnet?"
]

load_dotenv()

# Load Discord authorization token from environment variable
token = os.getenv('DISCORD_TOKEN')
if not token:
    print('ERROR: DISCORD_TOKEN environment variable is not set.')
    exit()

header = {'authorization': token}

def send_message(message):
    payload = {'content': message}

    try:
        r = requests.post(
            '<YOUR_CHANNEL_ID>', 
            data=payload,
            headers=header
        )
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print(f'HTTP error: {errh}')
    except requests.exceptions.ConnectionError as errc:
        print(f'Error connecting: {errc}')
    except requests.exceptions.Timeout as errt:
        print(f'Request timed out: {errt}')
    except requests.exceptions.RequestException as err:
        print(f'Error occurred: {err}')

def every_hour():
    random.shuffle(messages)

    for message in messages:
        send_message(message)
        time.sleep(random.randint(120, 140))

while True:
    every_hour()
    time.sleep(3600)


#Randomised the order of messages every hour
#Randomised the time interval between all the messages sent every hour
