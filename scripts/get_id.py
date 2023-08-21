from googleapiclient.discovery import build

def find_filename_by_id(file_name, creds):
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