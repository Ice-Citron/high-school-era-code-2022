from __future__ import print_function

from googleapiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

from datetime import datetime
from datetime import date

import time as t

import os
import json
import pickle

import json

import numpy as np

from functions import function_check, function_input
from typing import Optional

from undo import undo_input


class token():

    def __init__(self):

        self.store = file.Storage('token.json')


    def return_form_service(self):

        SCOPES = ["https://www.googleapis.com/auth/forms.body",
                  "https://www.googleapis.com/auth/forms.responses.readonly",
                  "https://www.googleapis.com/auth/userinfo.email",
                  'https://www.googleapis.com/auth/drive']

        DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

        if os.path.exists('token.json'):

            with open('token.json') as json_file:
                creds = json.load(json_file)

            user_encode_data = json.dumps(creds, indent=2).encode('utf-8')

            creds = client.OAuth2Credentials.from_json(user_encode_data)

        else:

            creds = None


        if not creds or creds.invalid:
            
            flow = client.flow_from_clientsecrets('Google form resource/client_secret_55707979508-6uvs9blojkdvm4e8mjsdok0n3ro794va.apps.googleusercontent.com.json', SCOPES)
            creds = tools.run_flow(flow, self.store)

            
        form_service = discovery.build('forms', 'v1', http=creds.authorize(
            Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

        drive_service = discovery.build('drive', 'v3', credentials=creds)
        

        return form_service, drive_service


    def check_id_existence(self):

        if os.path.exists('token.json'):

            with open('token.json') as json_file:
                creds = json.load(json_file)

            user_encode_data = json.dumps(creds, indent=2).encode('utf-8')

            creds = client.OAuth2Credentials.from_json(user_encode_data)

            return True

        else:

            creds = None


        if not creds or creds.invalid:

            return False


    def email_address(self):

        with open('token.json') as json_file:
            creds = json.load(json_file)

        email_address = creds['id_token']['email']

        return email_address


    def log_out(self):

        os.remove('token.json')
        '''calls in homepage function'''


    def refresh_token(self):
        #not required for now. might required is bakesell app doesn't get verified.

        pass



class function_forms():
    

    def __init__(self, datafile: dict, form_service: str, drive_service: str, folder_id: str):

        self.datafile = datafile
        self.chec = function_check(datafile = datafile)
        self.func = function_input(datafile = datafile)
        self.timestamp = datetime.now().timestamp()
        self.form_service = form_service
        self.drive_service = drive_service
        self.folder_id = folder_id
        self.undo     = undo_input()
    

    def output_data(self):

        dump_obj = json.dumps(self.datafile, indent = 4)

        with open("data.json", "w") as file:
            file.write(dump_obj) 


    def products_of_event(self, event: str):
        #event is the date, i.e '2/22'
        #this function returns all the products into a list for sale of a certain event. will be used for #create_form_input_order or #create_form_sell functions

        product = []
 
        lista = list(self.datafile['orders_tofill'][event])
        del lista[-1]
        listb = list(self.datafile['orders_tofill'][event]['special_occasion'])
        for i in range(len(listb)):
            lista.append(listb[i])

        return product


    def create_form_input_order(self):
        #products is the list of product that will be sent, e.g ['cake', 'coke', 'balloon']
        #event is the event name, e.g "Easter bakesell"
        #duedate will be timestamp of when the form needs to be inputted into the datastructure
        
        event = self.datafile['event'][0]
        
        products = self.products_of_event(event = event)
        event_name = self.datafile['event_name'][event]

        if self.datafile['form_id'][event]['input'] != 0:

            return f"There is already a google form for the event {event_name}. Delete the existing 'input_order' google form before creating a new one."
        
        undo_dicta = {'event': event}
        self.undo.new_action(action = 'create_form_input_order', param = undo_dicta, types = 'form')
        
        INPUT_FORM = {}

        INPUT_FORM['info'] = {}

        INPUT_FORM['info']['title'] = "{} order".format(event_name + ' - input')
        INPUT_FORM['info']['documentTitle'] = "{} order".format(event_name + ' - input')

        #input_order
        
        INPUT_ORDER = {}

        INPUT_ORDER['requests'] = []

        #updateFormInfo sub-dictionary
        uform = {}
        uform['updateFormInfo'] = {}
        uform['updateFormInfo']['info'] = {}
        uform['updateFormInfo']['info']['description'] = "Please enter your orders for {} bakesale.".format(event_name)
        uform['updateFormInfo']['updateMask'] = "description"
        
        INPUT_ORDER['requests'].append(uform)  

        #individual-create form list
        
        #initial cform asking for name
        cform = {}
        cform['createItem'] = {}
        cform['createItem']['item'] = {}
        cform['createItem']['item']['title'] = 'What is your name?'
        cform['createItem']['item']['questionItem'] = {}
        cform['createItem']['item']['questionItem']['question'] = {}
        cform['createItem']['item']['questionItem']['question']['questionId'] = '0fffffff'
        cform['createItem']['item']['questionItem']['question']['required'] = True
        cform['createItem']['item']['questionItem']['question']['textQuestion'] = {}
        cform['createItem']['location'] = {}
        cform['createItem']['location']['index'] = 0

        INPUT_ORDER['requests'].append(cform)
        
        #lists of cforms
        for i in range(len(products)):

            item_id = '0f' + str(f'{i:0>6}')

            cforms = {}
            cforms['createItem'] = {}
            cforms['createItem']['item'] = {}
            cforms['createItem']['item']['title'] = 'How much {} would you like? -enter 0 if none-'.format(products[i])
            cforms['createItem']['item']['questionItem'] = {}
            cforms['createItem']['item']['questionItem']['question'] = {}
            cforms['createItem']['item']['questionItem']['question']['questionId'] = item_id
            cforms['createItem']['item']['questionItem']['question']['required'] = True
            cforms['createItem']['item']['questionItem']['question']['textQuestion'] = {}
            cforms['createItem']['location'] = {}
            cforms['createItem']['location']['index'] = i + 1

            INPUT_ORDER['requests'].append(cforms)

        # Creates the input order form
        result = self.form_service.forms().create(body=INPUT_FORM).execute()

        # Adds the question to the form
        question_setting = self.form_service.forms().batchUpdate(formId=result["formId"], body=INPUT_ORDER).execute()

        # Prints the result to show the question has been added
        get_result = self.form_service.forms().get(formId=result["formId"]).execute()
        
        #adding FormID to the data structure
        self.datafile['form_id'][event]['input'] = get_result['formId']

        #move form into official folder for storage
        target_folder_id = self.folder_id

        self.drive_service.files().update(
            fileId = get_result['formId'],
            addParents = target_folder_id
            ).execute()
                
        self.output_data()
        self.chec.check_all()
            
        return get_result


    def delete_form_input_order(self):

        event = self.datafile['event'][0]

        event_name = self.datafile['event_name'][event]
        if self.datafile['form_id'][event]['input'] == 0:
            return "No input order google form is present for {event_name}."
        
        form_id = self.datafile['form_id'][event]['input']
        event_name = self.datafile['event_name'][event]

        self.drive_service.files().delete(fileId = form_id).execute()

        self.datafile['form_id'][event]['input'] = 0

        self.output_data()

        return "All clear"


    def delete_form_sell_order(self):

        event = self.datafile['event'][0]
        event_name = self.datafile['event_name'][event]
        if self.datafile['form_id'][event]['sell'] == 0:
            return "No sell order google form is present for {event_name}."

        form_id = self.datafile['form_id'][event]['input']
        event_name = self.datafile['event_name'][event]

        self.drive_service.files().delete(fileId = form_id).execute()

        self.datafile['form_id'][event]['input'] = 0

        self.output_data()

        return "All clear"
    

    def create_form_sell(self):
        #products is the list of product that have been sold, e.g ['cake', 'coke', 'balloon']
        #event is the event name
        #duedate will be timestamp of when the form needs to be inputted into the datastructure

        #this function creates a form order for the sellers to input the people who paid
        event = self.datafile['event'][0]
        
        products = self.products_of_event(event = event)
        event_name = self.datafile['event_name'][event]
        orders = self.datafile['orders_req_cancellation'][event]

        INPUT_FORM = {}

        INPUT_FORM['info'] = {}

        INPUT_FORM['info']['title'] = "{} order".format(event_name + ' - sell')
        INPUT_FORM['info']['documentTitle'] = "{} order".format(event_name + ' - sell')

        #new_form
        NEW_FORM = {}
        NEW_FORM['requests'] = []

        #calculate_section_IDs
        #individual section_IDs would be created which would be used for each pagebreakItems

        section_ID = []

        for i in range(len(orders)):#for i in range(len(self.datafile['orders_req_cancellation'][event])):

            section_ID.append('0a' + str(f'{i:0>6}'))


        #sell_order

        #pre_order
        pforms = {}
        pforms['createItem'] = {}
        pforms['createItem']['item'] = {}
        pforms['createItem']['item']['itemId'] = '0fffffff' #preorder - section ID
        pforms['createItem']['item']['pageBreakItem'] = {}
        pforms['createItem']['item']['title'] = 'Pre ordered'
        pforms['createItem']['item']['description'] = 'Here is the list of names of people who has pre-ordered products. Please choose the correct name.'
        pforms['createItem']['location'] = {}
        pforms['createItem']['location']['index'] = 0

        NEW_FORM['requests'].append(pforms)
        

        #new_order
        nforms = {}
        nforms['createItem'] = {}
        nforms['createItem']['item'] = {}
        nforms['createItem']['item']['itemId'] = '0eeeeeee' #neworder - section ID
        nforms['createItem']['item']['pageBreakItem'] = {}
        nforms['createItem']['item']['title'] = 'New order'
        nforms['createItem']['item']['description'] = 'Enter what are the products and the amount that has been ordered by the pupil. If none just enter 0.'
        nforms['createItem']['location'] = {}
        nforms['createItem']['location']['index'] = 1

        NEW_FORM['requests'].append(nforms)

        #new_initial_orders
        for i in range(len(products)):
            norder = {}
            norder['createItem'] = {}
            norder['createItem']['item'] = {} 
            norder['createItem']['item']['title'] = products[i]
            norder['createItem']['item']['questionItem'] = {}
            norder['createItem']['item']['questionItem']['question'] = {}
            norder['createItem']['item']['questionItem']['question']['textQuestion'] = {}
            norder['createItem']['location'] = {}
            norder['createItem']['location']['index'] = i + 2

            NEW_FORM['requests'].append(norder)
            
        #confirmation for new_initial_orders
        conorder = {}
        conorder['createItem'] = {}
        conorder['createItem']['item'] = {}
        conorder['createItem']['item']['title'] = 'Please confirm that you are creating a new order.'
        conorder['createItem']['item']['questionItem'] = {}
        conorder['createItem']['item']['questionItem']['question'] = {}
        conorder['createItem']['item']['questionItem']['question']['required'] = True
        conorder['createItem']['item']['questionItem']['question']['choiceQuestion'] = {}
        conorder['createItem']['item']['questionItem']['question']['choiceQuestion']['type'] = 'RADIO'
        conorder['createItem']['item']['questionItem']['question']['choiceQuestion']['options'] = []
        conorder['createItem']['item']['questionItem']['question']['choiceQuestion']['options'].append({'value': 'Yes', 'goToAction': 'SUBMIT_FORM'})
        conorder['createItem']['item']['questionItem']['question']['choiceQuestion']['options'].append({'value': 'No', 'goToAction': 'RESTART_FORM'})
        conorder['createItem']['location'] = {}
        conorder['createItem']['location']['index'] = 2 + len(products)

        NEW_FORM['requests'].append(conorder)
     

        #list of all pre-ordered names
        for i in range(len(orders)):
            #to sort out the products and the amount of products ordered
            len(products) #amount of products in the event

            listp = []
            for j in range(len(products)):
                if products[j] in orders[list(orders)[i]]:
                    listp.append(products[j])
                    listp.append(orders[list(orders)[i]][products[j]])
                else:
                    listp.append(products[j])
                    listp.append(0)

            title = "Products ordered:"

            for j in range(len(products)):
                sub_title = '{} = {}'.format(listp[j * 2], listp[j * 2 + 1])
                title = title + ' ' + sub_title
                if j != (len(products) - 1):
                    title = title + ','

            title = title + '.'

            
            #the initial page breaker
            name = {}
            name['createItem'] = {}
            name['createItem']['item'] = {}
            name['createItem']['item']['itemId'] = section_ID[i]
            name['createItem']['item']['pageBreakItem'] = {}
            name['createItem']['item']['title'] = list(orders)[i].title()
            name['createItem']['item']['description'] = title
            name['createItem']['location'] = {}
            name['createItem']['location']['index'] = 3 + len(products) + (i * len(products)) + i*2 

            NEW_FORM['requests'].append(name)
            

            #loop for the products of pre-ordered
            for j in range(len(products)):
                pre = {}
                pre['createItem'] = {}
                pre['createItem']['item'] = {}
                pre['createItem']['item']['title'] = products[j]
                pre['createItem']['item']['questionItem'] = {}
                pre['createItem']['item']['questionItem']['question'] = {}
                pre['createItem']['item']['questionItem']['question']['textQuestion'] = {}
                pre['createItem']['location'] = {}
                pre['createItem']['location']['index'] = 4 + len(products) + (i * len(products)) + i*2 + j

                NEW_FORM['requests'].append(pre)
           

            #confirmation of sell_order
            cforms = {}
            cforms['createItem'] = {}
            cforms['createItem']['item'] = {}
            cforms['createItem']['item']['title'] = 'Please confirm that this is {}.'.format(list(orders)[i].title())
            cforms['createItem']['item']['questionItem'] = {}
            cforms['createItem']['item']['questionItem']['question'] = {}
            cforms['createItem']['item']['questionItem']['question']['required'] = True
            cforms['createItem']['item']['questionItem']['question']['choiceQuestion'] = {}
            cforms['createItem']['item']['questionItem']['question']['choiceQuestion']['type'] = 'RADIO'
            cforms['createItem']['item']['questionItem']['question']['choiceQuestion']['options'] = []
            cforms['createItem']['item']['questionItem']['question']['choiceQuestion']['options'].append({'value': 'Yes', 'goToAction': 'SUBMIT_FORM'})
            cforms['createItem']['item']['questionItem']['question']['choiceQuestion']['options'].append({'value': 'No', 'goToAction': 'RESTART_FORM'})
            cforms['createItem']['location'] = {}
            cforms['createItem']['location']['index'] = 2 + (i+2) * (len(products) + 1) + i*1 

            NEW_FORM['requests'].append(cforms)
            
        
        #add_sections - 0
        SECTION_FORM = {}
        SECTION_FORM['requests'] = []

        sform = {}
        sform['createItem'] = {}    
        sform['createItem']['item'] = {}
        sform['createItem']['item']['title'] = "Is this a pre-order or a new-order? Please Select."
        sform['createItem']['item']['questionItem'] = {}
        sform['createItem']['item']['questionItem']['question'] = {}
        sform['createItem']['item']['questionItem']['question']['required'] = True
        sform['createItem']['item']['questionItem']['question']['choiceQuestion'] = {}
        sform['createItem']['item']['questionItem']['question']['choiceQuestion']['type'] = 'RADIO'
        sform['createItem']['item']['questionItem']['question']['choiceQuestion']['options'] = []
        sform['createItem']['item']['questionItem']['question']['choiceQuestion']['options'].append({'value': 'Pre-order', 'goToSectionId': '0fffffff'}) #preorder - Section ID
        sform['createItem']['item']['questionItem']['question']['choiceQuestion']['options'].append({'value': 'New-order', 'goToSectionId': '0eeeeeee'}) #neworder - Section ID
        sform['createItem']['location'] = {}
        sform['createItem']['location']['index'] = 0

        SECTION_FORM['requests'].append(sform)


        #calculate how many available sections

        #add_sections - 2
        ssform = {}
        ssform['createItem'] = {}
        ssform['createItem']['item'] = {}
        ssform['createItem']['item']['title'] = "Choose the name of the pupil who had pre-ordered."
        ssform['createItem']['item']['questionItem'] = {}
        ssform['createItem']['item']['questionItem']['question'] = {}
        ssform['createItem']['item']['questionItem']['question']['required'] = True
        ssform['createItem']['item']['questionItem']['question']['choiceQuestion'] = {}
        ssform['createItem']['item']['questionItem']['question']['choiceQuestion']['type'] = 'DROP_DOWN'
        ssform['createItem']['item']['questionItem']['question']['choiceQuestion']['options'] = []

        for i in range(len(list(orders))):       
            ssform['createItem']['item']['questionItem']['question']['choiceQuestion']['options'].append({'value': '{}'.format(list(orders)[i].title()),
                                                                                                                  'goToSectionId': '{}'.format(section_ID[i])})
        
        ssform['createItem']['location'] = {}
        ssform['createItem']['location']['index'] = 2

        SECTION_FORM['requests'].append(ssform)

        # Creates the initial form
        result = self.form_service.forms().create(body=INPUT_FORM).execute()

        # Adds the question to the form
        question_setting = self.form_service.forms().batchUpdate(formId=result["formId"], body=NEW_FORM).execute()

        question_setting = self.form_service.forms().batchUpdate(formId=result["formId"], body=SECTION_FORM).execute()

        # Prints the result to show the question has been added
        get_result = self.form_service.forms().get(formId=result["formId"]).execute()

        #adding FormID to the data structure
        self.datafile['form_id'][event]['sell'] = get_result['formId']

        #move form into official folder for storage
        target_folder_id = self.folder_id

        self.drive_service.files().update(
            fileId = get_result['formId'],
            addParents = target_folder_id
            ).execute()

        self.output_data()
        self.chec.check_all()

        return get_result


    def check_input_form_created(self):

        if self.datafile['event'] == []:
            return False
        
        event = self.datafile['event'][0]
        form_id = self.datafile['form_id'][event]['input']

        if form_id == 0:
            return False

        elif form_id != 0:
            return True


    def retrieve_responses_input(self):

        #outputs the form responses from input_orders
        event = self.datafile['event'][0]

        form_id = self.datafile['form_id'][event]['input']
        
        content = self.form_service.forms().get(formId=form_id).execute()
        result = self.form_service.forms().responses().list(formId=form_id).execute() #to get the responses submitted to the google form

        dicta = {} #dict for orders_req_cancellation
        products = [] #this is the products thats for sale on the input_form

        if result == {}:
            
            self.datafile['orders_req_cancellation'][event] = dicta
            self.output_data()
            self.chec.check_all()

            return dicta
        
        lena = len(content['items'])    #the length of the content's item folder
        lenb = len(result['responses']) #this is the length of the amount of responses submitted on the response dict

        contentid = {}
        contentid['name'] = '0fffffff'
        listx = []

        for i in range(lena):
            if content['items'][i]['questionItem']['question']['questionId'] == '0fffffff':
                listx.append(0)
            elif content['items'][i]['questionItem']['question']['questionId'][:5] == '0f000':
                listx.append(content['items'][i]['questionItem']['question']['questionId'])
            else:
                listx.append(0)

        for i in range(len(listx)):
            if listx[i] != 0:
                title = content['items'][i]['title']
                product_name = ''.join(title.split()[2:-7])
                products.append(product_name)
                contentid[product_name] = content['items'][i]['questionItem']['question']['questionId']

        for i in range(lenb):
            link = result['responses'][i]['answers']#link to where the response file is located
            name = link[contentid['name']]['textAnswers']['answers'][0]['value']
            dicta[name] = {}
            for j in range(len(products)):
                amount = link[contentid[products[j]]]['textAnswers']['answers'][0]['value']
                if amount != '0' and amount.isdigit():
                    dicta[name][products[j]] = int(amount)

        self.datafile['manual_orders_req_cancellation'][event] = dicta
        self.output_data()
        self.chec.check_all()
        
        return dicta


    def retrieve_responses_output(self):

        #outputs the form responses from seller_orders
        event = self.datafile['event'][0]

        form_id = self.datafile['form_id'][event]['sell']
        
        content = self.form_service.forms().get(formId=form_id).execute()
        result = self.form_service.forms().responses().list(formId=form_id).execute() #to get the responses submitted to the google form
        
        dicta = {} #dict which consists of the products sold
        contentid = {} #the Id of questions that needs retrieving
        
        products = [] #list of products sold

        #tag for initial question
        contentid['initial'] = content['items'][0]['questionItem']['question']['questionId']
        contentid['prequestion'] = content['items'][2]['questionItem']['question']['questionId']

        #to find all products in the list
        #find the index of the products in the list
        
        sub_list = [] #will contain all of the 'itemId' of the all the products sold
        for i in range(len(content['items'])):
            sub_list.append(content['items'][i]['itemId'])
        first_index = sub_list.index('0eeeeeee')
        last_index = sub_list.index('0a000000')
        sub_list = sub_list[first_index + 1:last_index - 1]
        
        for i in range(len(sub_list)):
            product_name = content['items'][i+4]['title']
            products.append(product_name)
            dicta[product_name] = 0

        contentid['neworder'] = {}
        contentid['preorder'] = {}

        for i in range(len(products)):
            contentid['neworder'][products[i]] = ''

        #to find the people in pre-order
        lenc = len(content['items'][2]['questionItem']['question']['choiceQuestion']['options']) #the length of pre-order dropdown list
        basenum =  5 + len(products)#this is the index of where the pre-order list begins
        sizenum =  2 + len(products)#this is the size of each pre-order list
        for i in range(lenc):
            the_name = content['items'][2]['questionItem']['question']['choiceQuestion']['options'][i]
            contentid['preorder'][the_name['value']] = {}
            for j in range(len(products)):
                contentid['preorder'][the_name['value']][products[j]] = ''

        for i in range(len(products)):
            contentid['neworder'][products[i]] = content['items'][i+4]['questionItem']['question']['questionId']

        for i in range(len(list(contentid['preorder']))):
            names = list(contentid['preorder'])[i]
            for j in range(len(products)):
                contentid['preorder'][names][products[j]] = content['items'][basenum + i*sizenum + 1 + j]['questionItem']['question']['questionId']

        #now to retrieve information for dicta
        for i in range(len(result['responses'])):
            
            link = result['responses'][i]['answers']
            order_type = link[contentid['initial']]['textAnswers']['answers'][0]['value'] #this will tell whether is it neworder of preorder for the result
            
            if order_type == 'Pre-order':
                
                prequestion_tag = contentid['prequestion']#prequestion tag
                name = link[prequestion_tag]['textAnswers']['answers'][0]['value']

                for j in range(len(products)):
                    
                    conlink = contentid['preorder'][name][products[j]]
                    amount = link[conlink]['textAnswers']['answers'][0]['value']
                    if amount != '0' and amount.isdigit():
                        dicta[products[j]] += int(amount)
                
            elif order_type == 'New-order':
                
                for j in range(len(products)):

                    conlink = contentid['neworder'][products[j]]
                    amount = link[conlink]['textAnswers']['answers'][0]['value']
                    if amount != '0' and amount.isdigit():
                        dicta[products[j]] += int(amount)

        revenue = 0
        for i in range(len(list(dicta))):
            product_name = list(dicta)[i]
            self.func.input_product_sold(amount = dicta[product_name], product = product_name)  

        del self.datafile['orders_tofill'][event]
        del self.datafile['orders_req_cancellation'][event]
        del self.datafile['manual_orders_req_cancellation'][event]
        self.output_data()
        self.chec.check_all()
        
        return dicta


    def check_google_forms(self):

        for i in range(len(self.datafile['event'])):

            event = self.datafile['event'][i]

            timestamp_sta = int(datetime.strptime((date.today().year + '/' + self.datafile['event'][i]), '%Y/%m/%d').timestamp()) #timestamp when the event starts
            timestamp_end = timestamp_sta + 86400
            timestamp_exp = timestamp_sta + 86400 + 432000 #timestamp when event expires /// or 5 days after the event ends /// 432 000 is 5 days in seconds
            time_now = int(int(t.time())) #timestamp of the time right now

            if  time_now > timestamp_sta: #if timestamp_sta has been passed
                
                #data from input_order form will be retrieved
                #sell_order form will be created
                
                self.retrieve_responses_input()
                self.create_form_sell()

            elif time_now > timestamp_end: #if timestamp_end has been passed
                
                #output_order is retrieved
                self.retrieve_responses_output()






