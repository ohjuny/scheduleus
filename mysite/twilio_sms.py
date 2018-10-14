import json
import os

from twilio.rest import Client
from twilio.twiml import messaging_response, voice_response

import quickstart as qs

# [START configuration]
TWILIO_ACCOUNT_SID = "AC5b635c588d37e4b52b7a2dc80206a985"
TWILIO_AUTH_TOKEN = "31f8afc06b5d534894c6d03b5862da6b"
TWILIO_NUMBER = "+18577021901"
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
