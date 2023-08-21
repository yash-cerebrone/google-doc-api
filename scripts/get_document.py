from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def find_document(document_id, creds):
    try:
        service = build('docs', 'v1', credentials=creds) #build('docs', 'v1', developerKey=API_KEY) 

        # Retrieve the documents contents from the Docs service.
        document = service.documents().get(documentId=document_id).execute()

        # print('The title of the document is: {}'.format(document.get('title')))
        # print(document.get('body'))
        return document
                
    except HttpError as err:
        print(err)