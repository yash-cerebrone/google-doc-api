from googleapiclient.discovery import build
from get_placeholders import find_placeholder
from get_document import find_document
from googleapiclient.errors import HttpError
from delete_content import delete_placeholder


def add_about_me(text: list, is_bullet: bool, document_id: int, creds):
    '''
    Adds the given text into the ABOUT ME placeholder.
    Args:
    - text (string): the text to add
    - is_bullet (boolean): If the text being added is a bullet point
    - document_id (string): The ID of the document
    - creds: OAuth credentials
    '''
    for t in text:
        indices=find_placeholder(find_document(document_id, creds), 'ABOUT ME')
        assert indices is not None, 'Placeholder not found'

        requests = [
            ### adding text (last point endIndex)
            {
                'insertText': {
                    'location': {
                        'index': indices[0],
                    },
                    'text': f'{text} \n'
                }
            },
        ]
        if is_bullet:
            requests.append(
                ## creating bullet points
                {
                    'createParagraphBullets': {
                        'range': {
                            'startIndex': indices[0],
                            'endIndex':  indices[0]
                        },
                        'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE',
                    }
                },
            )

        try:
            service = build('docs', 'v1', credentials=creds)
            result = service.documents().batchUpdate(
                documentId=document_id, body={'requests': requests}).execute()
        except HttpError as e:
            print(e)

    delete_placeholder('ABOUT ME', is_bullet, document_id, creds)

def add_summary_points(text: list, is_bullet: bool, document_id: int, creds):
    '''
    Adds the given text into the SUMMARY placeholder.
    Args:
    - text (string): the text to add
    - is_bullet (boolean): If the text being added is a bullet point
    - document_id (string): The ID of the document
    - creds: OAuth credentials
    '''
    for t in text:
        indices=find_placeholder(find_document(document_id, creds), 'SUMMARY POINTS')
        assert indices is not None, 'Placeholder not found'

        requests = [
            ### adding text (last point endIndex)
            {
                'insertText': {
                    'location': {
                        'index': indices[0],
                    },
                    'text': f'{text} \n'
                }
            },
        ]
        if is_bullet:
            requests.append(
                ## creating bullet points
                {
                    'createParagraphBullets': {
                        'range': {
                            'startIndex': indices[0],
                            'endIndex':  indices[0]
                        },
                        'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE',
                    }
                },
            )

        try:
            service = build('docs', 'v1', credentials=creds)
            result = service.documents().batchUpdate(
                documentId=document_id, body={'requests': requests}).execute()
        except HttpError as e:
            print(e)

    delete_placeholder('SUMMARY POINTS', is_bullet, document_id, creds)

def add_languages(text: list, is_bullet: bool, document_id:str, creds):
    '''
    Adds the given text into the LANGUAGES placeholder.
    Args:
    - text (string): the text to add
    - is_bullet (boolean): If the text being added is a bullet point
    - document_id (string): The ID of the document
    - creds: OAuth credentials
    '''
    for t in text:
        indices=find_placeholder(find_document(document_id, creds), 'LANGUAGES')
        assert indices is not None, 'Placeholder not found'

        requests = [
            ### adding text (last point endIndex)
            {
                'insertText': {
                    'location': {
                        'index': indices[0],
                    },
                    'text': f'{text}'
                }
            },
        ]
        if is_bullet:
            requests.append(
                ## creating bullet points
                {
                    'createParagraphBullets': {
                        'range': {
                            'startIndex': indices[0],
                            'endIndex':  indices[0]
                        },
                        'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE',
                    }
                },
            )

        try:
            service = build('docs', 'v1', credentials=creds)
            result = service.documents().batchUpdate(
                documentId=document_id, body={'requests': requests}).execute()
        except HttpError as e:
            print(e)

    delete_placeholder('LANGUAGES', is_bullet, document_id, creds)

def add_responsibility(text: list, is_bullet: bool, document_id: str, creds, n: int):
    '''
    Adds the given text into the RESPONSIBILITIES placeholder.
    Args:
    - text (string): the text to add
    - is_bullet (boolean): If the text being added is a bullet point
    - document_id (string): The ID of the document
    - creds: OAuth credentials
    - n (int): Number corresponding to responsibility
    '''
    for t in text:
        indices=find_placeholder(find_document(document_id, creds), f'RESPONSIBILITIES {n}')
        assert indices is not None, 'Placeholder not found'

        requests = [
            ### adding text (last point endIndex)
            {
                'insertText': {
                    'location': {
                        'index': indices[0],
                    },
                    'text': f'{t} \n'
                }
            },
        ]
        if is_bullet:
            requests.append(
                ## creating bullet points
                {
                    'createParagraphBullets': {
                        'range': {
                            'startIndex': indices[0],
                            'endIndex':  indices[0]
                        },
                        'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE',
                    }
                },
            )

        try:
            service = build('docs', 'v1', credentials=creds)
            result = service.documents().batchUpdate(
                documentId=document_id, body={'requests': requests}).execute()
        except HttpError as e:
            print(e)

    delete_placeholder(f'RESPONSIBILITIES {n}', is_bullet, document_id, creds)