import json
import os

from twilio.rest import Client
from twilio.twiml import messaging_response, voice_response

import quickstart as qs

# [START configuration]
TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_NUMBER = os.environ['TWILIO_NUMBER']
# [END configuration]

# from mysite import mysite as ms

def send_msg(from_user, to_phone_number, event_name, maxtime): #string, datetime
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    rv = client.messages.create(
        to="+" + to_phone_number,
        from_=TWILIO_NUMBER,
        body="User " + from_user + " requests to add you to the event: [" +
                event_name + "], do you wish to accept? Text YES or NO"
    )
    print(rv)
