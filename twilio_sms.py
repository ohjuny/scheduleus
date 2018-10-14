from twilio.rest import Client
import quickstart as qs
import json
from mysite import mysite as ms

def send_msg(phone_number, maxtime): #string, datetime
    with open("twilio.json", "r") as f:
        data = json.load(f)
    # Your Account SID from twilio.com/console
    account_sid = data['id']
    # Your Auth Token from twilio.com/console
    auth_token  = data['token']

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to= "+" + phone_number,
        # to = '19178608933',
        from_="+15162611863",
        body=str(qs.main(maxtime)))
        # body = 'https://www.googleapis.com/auth/calendar')

    print(message.sid)
