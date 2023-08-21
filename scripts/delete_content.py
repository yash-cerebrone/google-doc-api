from googleapiclient.discovery import build
from get_placeholders import find_placeholder
from get_document import find_document
from googleapiclient.errors import HttpError

def delete_placeholder(text, is_bullet, document_id, creds):
    indices=find_placeholder(find_document(document_id, creds), text)
    try:
        assert(indices is not None)
    except Exception as e:
        print(e)
    print(indices)
    
    requests=[]
    if is_bullet:
        requests.append(
            ### removing bullet points
            {
                'deleteParagraphBullets': {
                    'range': {
                        'startIndex': indices[0],
                        'endIndex':  indices[1]
                    },
                }
            },
        )
    requests.append(
        ### deleting text (startIndex-1)
        {
            'deleteContentRange': {
                'range': {
                    'startIndex': indices[0],
                    'endIndex': indices[1],
                }
            }
        },
    )

    try:
        service = build('docs', 'v1', credentials=creds)
        result = service.documents().batchUpdate(
            documentId=document_id, body={'requests': requests}).execute()
    except HttpError as e:
        print(e)