from twilio.rest import Client
import quickstart as qs
import json
from mysite import mysite as ms


with open("twilio.json", "r") as f:
    data = json.load(f)
# Your Account SID from twilio.com/console
account_sid = data['id']
# Your Auth Token from twilio.com/console
auth_token = data['token']

client = Client(account_sid, auth_token)

message = client.messages.create(
    # to= "+" + "ms.account.models.Profile.phone_number",
    to = '+19178608933',
    from_='+19082939588',
    # body=str(qs.main()))
    body = 'hello')
    # body = 'https://www.googleapis.com/auth/calendar')

print(message.sid)
