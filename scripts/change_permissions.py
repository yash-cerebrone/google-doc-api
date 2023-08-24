from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import re

def add_single_user_permission(email, role, document_id, creds):
    '''
    Adds Permission for a single user based on email address
    Args:
    - email (string): email address of the person to add
    - role (string): role to be given eg viewer, editor etc
    - document_id (string): The ID of the document
    - creds: OAuth credentials
    '''
    # assertion checks
    assert role in ['reader', 'writer', 'owner', 'commenter'], 'Incorrect Role Choice'
    assert re.search(r'[a-z0-9]+@[a-z]+\.[a-z]{2,3}', email) is not None, 'Incorrect Email'

    # change single permission for user
    user_permission = {
                'type': 'user', 
                'role': role,
                'emailAddress': email
            }

    try:
        service = build('drive', 'v3', credentials=creds)
        service.permissions().create(fileId=document_id,
                                    body=user_permission,
                                    fields='id',).execute()
    except HttpError as error:
            print(F'An error occurred: {error}')

def add_domain_permission(domain, role, document_id, creds):
    '''
    Adds Permission for a domain based on company email address
    Args:
    - domain (string): domain of the organization to add
    - role (string): role to be given eg viewer, editor etc
    - document_id (string): The ID of the document
    - creds: OAuth credentials
    '''
    # assertion checks
    assert role in ['reader', 'writer', 'owner', 'commenter'], 'Incorrect Role Choice'
    assert re.search(r'^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" +"+[A-Za-z]{2,6}', domain) is not None, 'Incorrect Email'

    # change single permission for user
    domain_permission = {
                'type': 'domain', 
                'role': role,
                'domain': domain
            }

    try:
        service = build('drive', 'v3', credentials=creds)
        service.permissions().create(fileId=document_id,
                                    body=domain_permission,
                                    fields='id',).execute()
    except HttpError as error:
            print(F'An error occurred: {error}')

def add_batch(emails: dict, domains: dict, document_id: str, creds):
    '''
    Adds Permission for multiple people and domain
    Args:
    - emails (dict): email address of the persons to add (email-role in key-value pair)
    - domains (dict): domains of the organization to add (domain-role in key-value pair)
    - document_id (string): The ID of the document
    - creds: OAuth credentials
    '''

    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)
        ids = []

        def callback(request_id, response, exception):
            if exception:
                # Handle error
                print(exception)
            else:
                print(f'Request_Id: {request_id}')
                print(F'Permission Id: {response.get("id")}')
                ids.append(response.get('id'))

        # pylint: disable=maybe-no-member
        batch = service.new_batch_http_request(callback=callback)
        
        if emails is not None:
            if len(emails):
                for em, roles in emails.items():
                    user_permission = {
                        'type': 'user',
                        'role': roles,
                        'emailAddress': em
                    }
                    batch.add(service.permissions().create(fileId=document_id,
                                                        body=user_permission,
                                                        fields='id',))
        
        if domains is not None:
            if len(domains):
                for dom, roles in domains.items():
                    domain_permission = {
                        'type': 'domain',
                        'role': roles,
                        'domain': dom
                    }
                    batch.add(service.permissions().create(fileId=document_id,
                                                        body=domain_permission,
                                                        fields='id',))
        batch.execute()

    except HttpError as error:
        print(F'An error occurred: {error}')
        ids = None

    # return ids

def global_permission(role, document_id, creds):
    '''
    Sets global permissions rules for specific roles.
    Args:
    - role (string): role to be given eg viewer, editor etc
    - document_id (string): The ID of the document
    - creds: OAuth credentials
    '''
    assert role in ['reader', 'writer', 'commenter'], 'Incorrect Role Choice'

    globe_permission = {
                'type': 'anyone', 
                'role': role,
            }

    try:
        service = build('drive', 'v3', credentials=creds)
        service.permissions().create(fileId=document_id,
                                    body=globe_permission,
                                    fields='id',).execute()
    except HttpError as error:
            print(F'An error occurred: {error}')