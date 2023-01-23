from flask import Flask, request, jsonify

# This file is the basic flask server that will expose the endpoints needed to send and 
# receive emails using the gmail API. 

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

# This endpoint is going to be the one subscribed for push notifications 
# through the google cloud pub/sub api. Meaning when there is a published email event,
# this endpoint will be notified. 
# On my computer, if you're running locally, you post to this at http://127.0.0.1:5000/email
# Once this flask server has a real home, the endpoint needs to be added here: https://console.cloud.google.com/cloudpubsub/subscription/create?tutorial=pubsub--publish_receive_messages_console&project=milwaukeemakerspacebot&tab=messages
@app.route('/email', methods=["POST"])
def new_email_received():
    print("email received")
    print(request.json)

@app.route('/email', methods=["GET"])
def get_emails():
    print("you looking for emails?")
    return '<h1>Looking for emails?</h1>'