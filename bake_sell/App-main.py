from functions import function_input, function_check, data_retrieve, data_save, drive_check, undo_init, connection_check
from forms import function_forms, token
from undo import undo_func

#import sys
#sys.path.insert(1, 'GUI/Login page')sys.path.insert(1, 'GUI/dashboard')


form_service, drive_service = token().return_form_service()

folder_id = drive_check(drive_service = drive_service)
data, data_fileId = data_retrieve(drive_service = drive_service, folder_id = folder_id)
#note that data_fileId is the fileId for data.json in the drive

func = function_input(datafile = data)
chec = function_check(datafile = data)
'''
form = function_forms(datafile = data,
                      form_service = form_service,
                      drive_service = drive_service,
                      folder_id = folder_id)

undo = undo_func(datafile = data,
                 undofile = undo_init(),
                 form_service = form_service,
                 drive_service = drive_service,
                 folder_id = folder_id
                 )'''


##########################################################################################################################################################################################################

#connection check
if connection_check() == False:
    print('No connection available.') #function to prevent logging in etc

##########################################################################################################################################################################################################

#runs each time when system boots up
#each 12 hours reboot forms and chec.check_all() #create function to refresh forms input
 
chec.check_all()

#every 5 minutes upload data.json to cloud

data_save(
    drive_service = drive_service,
    data_fileId = data_fileId,
    folder_id = folder_id
    )

#every 1 hour check google forms
form.check_google_forms()

##########################################################################################################################################################################################################


chec.check_all()

#redo button: self.undo.redo()
#undo button: self.undo.undo()


##########################################################################################################################################################################################################















































