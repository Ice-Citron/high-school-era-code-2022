
##########################################################################################################################################################################################################
'''
#SCOPES = "https://www.googleapis.com/auth/forms.body" #enable if creating new gform, or viewing contents of gform
#SCOPES = "https://www.googleapis.com/auth/forms.responses.readonly"  #enable if viewing all responses
SCOPES = ["https://www.googleapis.com/auth/forms.body", "https://www.googleapis.com/auth/forms.responses.readonly"]

DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

store = file.Storage('token.json')



if os.path.exists('token.json'):

    with open('token.json') as json_file:
        creds = json.load(json_file)

    user_encode_data = json.dumps(creds, indent=2).encode('utf-8')

    creds = client.OAuth2Credentials.from_json(user_encode_data)

else:

    new_main_dict = {}

    dump_obj = json.dumps(new_main_dict, indent = 4)

    with open("data.json", "w") as datafile:
        datafile.write(dump_obj)

    with open("data.json", "r") as datafile:
        creds = json.load(datafile)


if not creds or creds.invalid:
    
    flow = client.flow_from_clientsecrets('Google form resource/client_secret_55707979508-6uvs9blojkdvm4e8mjsdok0n3ro794va.apps.googleusercontent.com.json', SCOPES)
    creds = tools.run_flow(flow, store)


    
form_service = discovery.build('forms', 'v1', http=creds.authorize(
    Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)'''


##########################################################################################################################################################################################################

'''
# Creates the initial form
result = form_service.forms().create(body=NEW_FORM).execute()

# Adds the question to the form
question_setting = form_service.forms().batchUpdate(formId=result["formId"], body=NEW_QUESTION).execute()

question_setting = form_service.forms().batchUpdate(formId=result["formId"], body=SECTION_ADD).execute()

# Prints the result to show the question has been added
get_result = form_service.forms().get(formId=result["formId"]).execute()
print(get_result)'''

##########################################################################################################################################################################################################

'''
# Creates the input order form
result = form_service.forms().create(body=INPUT_FORM).execute()

# Adds the question to the form
question_setting = form_service.forms().batchUpdate(formId=result["formId"], body=INPUT_ORDER).execute()

# Prints the result to show the question has been added
get_result = form_service.forms().get(formId=result["formId"]).execute()
print(get_result)'''

##########################################################################################################################################################################################################

#view response or get content
'''
service = discovery.build('forms', 'v1', http=creds.authorize(
    Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

#form_id = '16SdvbeojrUAOzLSsCoMXpFKEfj5m9nhiA0EsR2isUKk' # quickstart form

form_id = '1pPr__Ml7b-oZE7tgRLdVlHpIFJG-U6Nu_y3Fh2iF9TU'

result = service.forms().get(formId=form_id).execute() #to get the content of the google form

#result = service.forms().responses().list(formId=form_id).execute() #to get the responses submitted to the google form
print(result)'''

##########################################################################################################################################################################################################



