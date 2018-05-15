import json

import httplib2
from googleapiclient import discovery

from DProject.Models.MessageInfo import MessageInfo
from DProject.Controler.gmail import get_credentials
from django.http import HttpResponse


def getGmail(request):
    """Shows basic usage of the Gmail API.

    Creates a Gmail API service object and outputs a list of label names
    of the user's Gmail account.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    # results = service.users().labels().list(userId='me').execute()
    results = service.users().messages().list(userId='me', labelIds=['UNREAD', 'INBOX'], q=None, maxResults=10).execute()
    messages = results.get('messages', [])
    list_messages = []
    message_from = ""
    message_subject = ""
    json_string = ""
    if not messages:
        print('No labels found.')
    else:
        print('ids:')
        for message in messages:
            results2 = service.users().messages().get(userId='me', id=message['id'],format="metadata").execute()
            headers = (results2.get('payload', [])).get('headers',[])

            for info in headers:
                if info['name'] == 'Subject':
                    message_subject = info['value']
                elif info['name'] == 'From':
                    message_from = info['value']

            # Method JSON Encoding

            message_details = results2.get('snippet', [])

            mInfo = MessageInfo(message_from,message_subject,message_details)

            # list of messages
            list_messages.append(mInfo)

            # conversion to json ENCODING
            json_string = json.dumps([mInfo.__dict__ for mInfo in list_messages ])

    return HttpResponse(json_string)