from get_credentials import main
from get_id import find_id_by_filename
from get_placeholders import find_placeholder
from delete_content import delete_placeholder
from get_document import find_document
from misc import create_duplicate
from add_content import *
from change_permissions import *

file_name=input('Enter filename: ')
creds=main()

DOCUMENT_ID=find_id_by_filename(file_name, creds)
assert DOCUMENT_ID is not None, 'No file found'

global_permission('reader', DOCUMENT_ID, creds)
# add_single_user_permission('yash.chauhan062@nmims.edu.in','reader', DOCUMENT_ID, creds)

# responsibilites=['this is responsibility 1', 'this is responsibility 2', 'this is responsibility 3', 'this is responsibility 4']

# add_responsibility(responsibilites, True, DOCUMENT_ID, creds, 1)

# print(find_placeholder(document, 'RESPONSIBILITIES 1'))