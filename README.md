# DiscordGoogleGroupBridge
A bridge between the MMS discord and google group 

# Set-up
Create a venv: https://docs.python.org/3/library/venv.html
I created mine with python 3.10 but do what feels good. 
Install requirements: pip install -r requirements.txt


# Coding journal
20221229

Goals:
- the discord bot is minimal and viable, but it needs to actually have two event notifications for when a new message is published? (should it send directly or cache the messages?)
- The email watcher is the hard part: I would rather it work by subscription than by polling, google console offers a pub sub service for this reason. There is documentation for pub sub with the gmail api [here](https://developers.google.com/gmail/api/guides/push)
- The flask server will actually expose endpoints that can be used for the subscription. 
- The email_utilites is what's going ot be the meat and potatoes of the business logic for the endpoints. 

Goal is to setup the pub sub with an emulator. The emulator just allows me to have an endpoint on my local machine, rather than actually propping up this little flask server with a visible ip somewhere. Documentation used can be found [here](https://cloud.google.com/pubsub/docs/emulator#windows) and [here]()

Let's get one direction working. To do this, I am going to use the emulator to set-up fake email notifications, these will have to mock the structure of real gmail api notifications. 


