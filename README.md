# Discord-Message-Bot
This discord messaging bot automates the sending of a list of messages, which are shuffled every hour and delivered at random times. This was a fun project built for experimentational purposes. There are better security practices you can further implement on top of this project to protect your authorization ID.

##Steps to use this bot

###Clone the repo

```
https://github.com/mcgrathcoutinho/discord-message-bot.git
```

###Installations

1. Check if you have pip using:
```
pip --version
```

2. If you do not have pip, run the following commands:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

3. Install dotenv using:
```
pip install python-dotenv
```

###Create an environment variable file:
```
touch .env
```

###In the environment variable file, type:
```
DISCORD_TOKEN="<YOUR_AUTHORIZATION_ID_HERE>"
```
Use the following youtube video for reference on getting your authorization id: https://www.youtube.com/watch?v=DArlLAq56Mo

###Replace <YOUR_CHANNEL_ID> in the discord-message.py script 

Replace it with the channel ID you want to automate messages to. Again for this, refer to the youtube video above to see how to access it.

###Run your script:
```
python discord-message.py
```
If you come across any HTTP errors, CTRL+C in your terminal to terminate the script from running. You can then try re-running the script.
