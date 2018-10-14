from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os
#import mysite/events.models

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'

def main(): #maxtime):
    """Gets information from Google Calendar and sets database freetime information
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        flags = tools.argparser.parse_args(args=[])
        creds = tools.run_flow(flow, store, flags)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    # get 50 events for now
    events_result = service.events().list(calendarId='primary',# timeMax=maxtime, 
                                        timeMin=now,
                                        maxResults=4, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    listOfDateTimes=[]
    for event in events:
        start = event['start'].get('dateTime')
        end = event['end'].get('dateTime')

        print(event['summary'], "test", start, end)

        starttemp = str(start).split('T')
        endtemp = str(end).split('T')

        wholeDay = len(starttemp)
        startdate = starttemp[0]
        enddate = endtemp[0]

        if(wholeDay-1):
            starttime = starttemp[1].split(':')
            starttimef = starttime[0]+':'+starttime[1]
            
            endtime = endtemp[1].split(':')
            endtimef = endtime[0] +':'+endtime[1]
        else:
            startdate = str(start)
            enddate = str(end)

        listOfDateTimes.append(startdate + ' ' + starttimef)
        listOfDateTimes.append(enddate + ' ' + endtimef) 

    if os.path.exists("token.json"):
        os.remove("token.json")
        
    return listOfDateTimes

if __name__ == '__main__':
    main()