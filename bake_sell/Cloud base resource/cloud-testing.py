from forms import token
from googleapiclient import discovery
import json
from oauth2client import client, file, tools
from httplib2 import Http

CSF = 'Google form resource/client_secret_55707979508-6uvs9blojkdvm4e8mjsdok0n3ro794va.apps.googleusercontent.com.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ["https://www.googleapis.com/auth/forms.body",
                  "https://www.googleapis.com/auth/forms.responses.readonly",
                  "openid",
                  "https://www.googleapis.com/auth/userinfo.email",
                  'https://www.googleapis.com/auth/drive']

#service = create_service(CSF, API_NAME, API_VERSION, SCOPES)
#print('google drive API')
#print(service)
#service = token().return_form_service()
#print('google form API')
#print(service)

with open('token.json') as json_file:
    creds = json.load(json_file)

user_encode_data = json.dumps(creds, indent=2).encode('utf-8')

creds = client.OAuth2Credentials.from_json(user_encode_data)

service = discovery.build('drive', 'v3', credentials=creds)#.authorize(
           # Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)


#moving file into a folder
'''
target_folder_id = '1KyqfXGSe2DQ7Pt-UwRZZy77-tTCnVSSo'

service.files().update(
    fileId = '14NX8cA816CPqz2ScefyhTs86kRzw1iU-rkTs_4EsPvg',
    addParents = target_folder_id
    ).execute()'''


#creating a new folder

file_metadata = {
    #'name': 'Data_storage_for_bakesale_app-DO_NOT_DELETE',
    'name': 'hello_world_223',
    'mimeType': 'application/vnd.google-apps.folder',
    #'id': 'Bake-Sale-App-Data-Storage-Folder'
    }

item_id = service.files().create(body = file_metadata).execute()['id']

print(item_id)#the id of the folder


#uploading data of config file
'''
from googleapiclient.http import MediaFileUpload

folder_id = '1uXDeOH6BoAhCzwasxdff85PD-ZuoZ_f-'
file_name = 'data.json'
mime_type = 'application/vnd.google-apps.script+json'

file_metadata = {
    'name': 'data - ss s.json',
    'parents': [folder_id],
    }

media = MediaFileUpload(file_name, mimetype = 'text/plain')
#creating a brand new file
service.files().create(
    body = file_metadata,
    media_body = media,
    fields='id'
    ).execute()

#replacing the data of a file
print(service.files().update(
    fileId = '100M1pHgz1azMZqnpeIq3sB0TroF103FZ',
    media_body = media).execute())'''


#retrieve data of config file
'''
import json
import io
import os
from googleapiclient.http import MediaIoBaseDownload


result = service.files().get_media(
    fileId   = '100M1pHgz1azMZqnpeIq3sB0TroF103FZ',
    )
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, result)
done = False

while done is False:
    status, done = downloader.next_chunk()
    print("Download %d%%." % int(status.progress() * 100))
fh.seek(0)

with open(os.path.join('data copy.json'), 'wb') as f:
    f.write(fh.read())
    f.close()

print(fh.read().decode("utf-8") )
'''

#finding id of a file
'''
query = f"parents = '{'1uXDeOH6BoAhCzwasxdff85PD-ZuoZ_f-'}'"
results = service.files().list(
    q = query,
    fields  = "nextPageToken, files(id, name)").execute()
#items = results.get('files', [])
print(results)
'''

#checking if folder exists in google drive
'''
response = service.files().list(
    q="name='Data_storage_for_bakesale_app-DO_NOT_DELETE' and mimeType='application/vnd.google-apps.folder'",
).execute()

if response['files'] == []:
    print(False)
    print(response)
else:
    print(True)
    print(response)'''

#deleting a file
'''
service.files().delete(fileId = '1Na6LGTUgEVW3KZJ7UA7OFohxb8PdPF3j').execute()
'''





