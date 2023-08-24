from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from get_id import find_filename_by_id, find_id_by_filename
import datetime as dt

def get_link(document_id: str):
    '''
    Returns the link of the document id
    Args:
    - document_id (string): The document id to generate the link for
    Returns:
    - Link for the document
    '''
    return f'docs.google.com/document/d/{document_id}'

def create_duplicate(source_id: str, creds, link: bool=False):
    '''
    Creates duplicate file
    Args:
    - source_id (string): creates a duplicate file for the given source document id
    - creds: OAuth credentials
    - link (bool): To check if link should be returned or only id
    Returns:
    - The ID/link of the duplicated document
    '''
    try:
        # Build the Google Drive API client
        drive_service = build('drive', 'v3', credentials=creds)
        # ID of the file you want to duplicate
        source_file_id = source_id

        # Define the new name for the duplicated file
        file_name=find_filename_by_id(source_id, creds)
        new_name = f'{file_name} new {dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'

        # Create a copy of the file
        duplicate_file = {
            'name': new_name
        }

        drive_service.files().copy(fileId=source_file_id, body=duplicate_file).execute()

        if link:
            return get_link(find_id_by_filename(new_name, creds))
        else:
            return find_id_by_filename(new_name, creds)
    except HttpError as e:
        print(e)