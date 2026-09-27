##########################################################################################################################################################################################################
'''for sales order'''
#create page breaker first. then update by adding in questions.
NEW_QUESTION = {
    "requests": [{
        "createItem": {
            "item": {'itemId': '47df46f7',
                     'pageBreakItem': {},
                     'title': 'Pre-ordered',
                     'description': 'qwerty'},
            "location": {
                "index": 0
            }
       }
    },{
        "createItem": {
            "item": {'itemId': '7856a3d6',
                     'pageBreakItem': {},
                     'title': 'New order',
                     'description': 'Enter what are the products and the amount that has been ordered. If none just enter 0'},
            "location": {
                "index": 1 #New order
            }
            }
    },{
        "createItem": {
            "item": {'itemId': '549079c7',
                     'title': 'cake ',
                     'questionItem': {'question':
                                      {'questionId': '24e44c3e',
                                       'textQuestion': {}}}},
            "location": {
                "index": 2 #New order - 1
            }
            }
    },{
        "createItem": {
            "item": {'itemId': '52d4e476',
                     'title': 'coke',
                     'questionItem': {'question':
                                      {'questionId': '5c5e752f',
                                       'textQuestion': {}}}},
            "location": {
                "index": 3 #New order - 2
            }
            }
    },{
        "createItem": {
            "item": {'itemId': '1b67992a',
                     'title': 'balloon',
                     'questionItem': {'question':
                                      {'questionId': '1021b451',
                                       'textQuestion': {}}}},
            "location": {
                "index": 4 #New order - 3
            }
            }
    },{
        "createItem": {
            "item": {'itemId': '21c8b324',
                     'title': 'Please confirm that you are creating a new order.',
                     'questionItem': {'question': {'questionId': '1c9996cd',
                                                   'required': True,
                                                   'choiceQuestion': {'type': 'RADIO',
                                                                      'options': [{'value': 'Yes',
                                                                                   'goToAction': 'SUBMIT_FORM'},
                                                                                  {'value': 'No',
                                                                                   'goToAction': 'RESTART_FORM'}
                                                                                  ]}}}},
            "location": {
                "index": 5 #New order - confirm
            }
            }
    },{
        "createItem": {
            "item": {'itemId': '4da7e4b1',
                     'pageBreakItem': {},
                     'title': 'nimbus 1',
                     'description': 'product ordered: cake = 5, coke = 2, balloon = 2'},
            "location": {
                "index": 6 #Nimbus 1
            }
            }
    },{
        "createItem": {
            "item": {'itemId': '416d623f',
                     'title': 'cake',
                     'questionItem': {'question':
                                      {'questionId': '33c6e987',
                                       'textQuestion': {}}}},
            "location": {
                "index": 7 #Nimbus 1 - 1
            }
            }
    },{
        "createItem": {
            "item": {'itemId': '4c764f28',
                     'title': 'coke',
                     'questionItem': {'question':
                                      {'questionId': '08790319',
                                       'textQuestion': {}}}},
            "location": {
                "index": 8 #Nimbus 1 - 2
            }
            }
    },{
        "createItem": {
            "item": {'itemId': '31e37573',
                     'title': 'balloon',
                     'questionItem': {'question':
                                      {'questionId': '06a81662',
                                       'textQuestion': {}}}},
            "location": {
                "index": 9 #Nimbus 1 - 3
            }
            }
    },{
        "createItem": {
            "item": {'itemId': '78debf36',
                     'title': 'Please confirm that this is Nimbus 1.',
                     'questionItem': {'question': {'questionId': '624f7a65',
                                                   'required': True,
                                                   'choiceQuestion': {'type': 'RADIO',
                                                                      'options': [{'value': 'Yes',
                                                                                   'goToAction': 'SUBMIT_FORM'},
                                                                                  {'value': 'No',
                                                                                   'goToAction': 'RESTART_FORM'}
                                                                                  ]}}}},
            "location": {
                "index": 10 #Nimbus 1 - confirm
            }
            }
    },{
        "createItem": {
            "item": {'itemId': '2b233b18',
                     'pageBreakItem': {},
                     'title': 'nimbus 2',
                     'description': 'product ordered: cake = 7, coke = 2, balloon = 3'},
            "location": {
                "index": 11 #Nimbus 2
            }
            }
    },{
        "createItem": {
            "item": {'itemId': '726f3506',
                     'title': 'cake',
                     'questionItem': {'question':
                                      {'questionId': '55d33eda',
                                       'textQuestion': {}}}},
            "location": {
                "index": 12 #Nimbus 2 - 1
            }
            }
    },{
        "createItem": {
            "item": {'itemId': '3b349b01',
                     'title': 'coke',
                     'questionItem': {'question':
                                      {'questionId': '4a21e9c9',
                                       'textQuestion': {}}}},
            "location": {
                "index": 13 #Nimbus 2 - 2
            }
            }
    },{
        "createItem": {
            "item": {'itemId': '2fc0f52b',
                     'title': 'balloon',
                     'questionItem': {'question':
                                      {'questionId': '140d5f4f',
                                       'textQuestion': {}}}},
            "location": {
                "index": 14 #Nimbus 2 - 3
            }
            }
    },{
        "createItem": {
            "item": {'itemId': '505708bc',
                     'title': 'Please confirm that this is Nimbus 2.',
                     'questionItem': {'question': {'questionId': '0c0b8228',
                                                   'required': True,
                                                   'choiceQuestion': {'type': 'RADIO',
                                                                      'options': [{'value': 'Yes',
                                                                                   'goToAction': 'SUBMIT_FORM'},
                                                                                  {'value': 'No',
                                                                                   'goToAction': 'RESTART_FORM'}
                                                                                  ]}}}},
            "location": {
                "index": 15 #Nimbus 2 - confirm
            }
            }
    },{
        "createItem": {
            "item": {'itemId': '62c31f6c',
                     'pageBreakItem': {},
                     'title': 'nimbus 3',
                     'description': 'product ordered: cake = 4, coke = 1, balloon = 2'},
            "location": {
                "index": 16 #Nimbus 3
            }
            }
    },{
        "createItem": {
            "item": {'itemId': '3086fdbb',
                     'title': 'cake',
                     'questionItem': {'question':
                                      {'questionId': '6488e79f',
                                       'textQuestion': {}}}},
            "location": {
                "index": 17 #Nimbus 3 - 1
            }
            }
    },{
        "createItem": {
            "item": {'itemId': '6933b9b8',
                     'title': 'coke',
                     'questionItem': {'question':
                                      {'questionId': '0441ac57',
                                       'textQuestion': {}}}},
            "location": {
                "index": 18 #Nimbus 3 - 2
            }
            }
    },{
        "createItem": {
            "item": {'itemId': '73b87f82',
                     'title': 'balloon',
                     'questionItem': {'question':
                                      {'questionId': '46ffcfb6',
                                       'textQuestion': {}}}},
            "location": {
                "index": 19 #Nimbus 3 - 3
            }
            }
    },{
        "createItem": {
            "item": {'itemId': '2ff21c5a',
                     'title': 'Please confirm that this is Nimbus 3.',
                     'questionItem': {'question': {'questionId': '645e2cea',
                                                   'required': True,
                                                   'choiceQuestion': {'type': 'RADIO',
                                                                      'options': [{'value': 'Yes',
                                                                                   'goToAction': 'SUBMIT_FORM'},
                                                                                  {'value': 'No',
                                                                                   'goToAction': 'RESTART_FORM'}
                                                                                  ]}}}},
            "location": {
                "index": 20 #Nimbus 3 - confirm
            }
            }
    }
                 ]
}

##########################################################################################################################################################################################################

#specific questions that will be added.
SECTION_ADD = {
    "requests": [{
        "createItem": {
            "item": {'itemId': '2b414436',
                     'title': 'is it a pre-ordered or a new order',
                     'questionItem': {'question':
                                      {'questionId': '16271a0f',
                                       'required': True,
                                       'choiceQuestion': {'type': 'RADIO',
                                                          'options': [{'value': 'pre-order',
                                                                       'goToSectionId': '47df46f7'},
                                                                      {'value': 'new-order',
                                                                       'goToSectionId': '7856a3d6'}
                                                                      ]}}}},
            "location": {
                "index": 0
            }
       }
    },{
        "createItem": {
            "item": {'itemId': '6871edc3',
                     'title': 'choose name',
                     'questionItem': {'question':
                                      {'questionId': '43814615',
                                       'required': True,
                                       'choiceQuestion': {'type': 'DROP_DOWN',
                                                          'options': [{'value': 'nimbus 1',
                                                                       'goToSectionId': '4da7e4b1'},
                                                                      {'value': 'nimbus 2',
                                                                       'goToSectionId': '2b233b18'},
                                                                      {'value': 'nimbus 3',
                                                                       'goToSectionId': '62c31f6c'}
                                                                      ]}}}},
            "location": {
                "index": 2
            }
       }
    }]
}


##########################################################################################################################################################################################################

'''for input order'''

event = "valentine's"

INPUT_FORM = {
    "info": {
        "title": "{} order".format(event),
        'documentTitle': "{} order".format(event)
    }
}

INPUT_ORDER = {
    "requests": [{
        "updateFormInfo": {
            'info': {
                'description': "Please enter your orders for {}.".format(event)},
            'updateMask': "description"
            }
        },{
        "createItem": {
            'item': {'itemId': '1244d41e',
                      'title': 'What is your name?',
                      'questionItem': {'question':
                                       {'questionId': '6b5fd3f3',
                                        'required': True,
                                        'textQuestion': {}}}},
            "location": {
                "index": 0
                }
            }
        },{
        "createItem": {
            'item': {'itemId': '708e9849',
                      'title': 'How much cake would you like?',
                      'questionItem': {'question':
                                       {'questionId': '32cceb2f',
                                        'required': True,
                                        'textQuestion': {}}}},
            "location": {
                "index": 1
                }
             }
        },{
        "createItem": {
            'item': {'itemId': '368ec1ac',
                      'title': 'How much coke would you like?',
                      'questionItem': {'question':
                                       {'questionId': '222fc5c4',
                                        'required': True,
                                        'textQuestion': {}}}},
            "location": {
                "index": 2
                }
            }
        },{
        "createItem": {
            'item': {'itemId': '6208c349',
                      'title': 'How much balloon would you like?',
                      'questionItem': {'question':
                                       {'questionId': '7b6cc12d',
                                        'required': True,
                                        'textQuestion': {}}}},
            "location": {
                "index": 3
                }
            }
        }]
    }



##########################################################################################################################################################################################################
