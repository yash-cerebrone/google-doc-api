from googleapiclient.discovery import build

def find_id_by_filename(file_name, creds):
    '''
    Returns id from the filename provided
    Args:
    - file_name (string): name of the file in the drive
    - creds: OAuth credentials
    Returns:
    - id (string): Document ID of the file
    '''
    # List files in your Google Drive
    drive_service = build('drive', 'v3', credentials=creds)

    results = drive_service.files().list().execute()
    files = results.get('files', [])

    if not files:
        print('No files found.')
    else:
        # print('Files:')
        for file in files:
            if file['name']==file_name:
                return file['id']
            
def find_filename_by_id(document_id, creds):
    '''
    Returns id from the filename provided
    Args:
    - document_id (string): id of the file in the drive
    - creds: OAuth credentials
    Returns:
    - name (string): Name of the file in the drive
    '''
    # List files in your Google Drive
    drive_service = build('drive', 'v3', credentials=creds)

    results = drive_service.files().list().execute()
    files = results.get('files', [])

    if not files:
        print('No files found.')
    else:
        # print('Files:')
        for file in files:
            if file['id']==document_id:
                return file['name']