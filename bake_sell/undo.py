import time
import json

#undo dict list for functions.py
undo_dict_func = {'input_cost': {'delete_cost': {'cost': 'cost'}},
                  'delete_cost': {'input_cost': {'cost': 'cost'}},
                  'input_product_made': {'delete_product_made': {'product': 'product', 'amount': 'amount'}},
                  'delete_product_made': {'input_product_made': {'product': 'product', 'amount': 'amount'}},
                  'input_time_spent': {'delete_time_spent': {'hour': 'hour', 'minute': 'minute'}},
                  'delete_time_spent': {'input_time_spent': {'hour': 'hour', 'minute': 'minute'}},
                  'input_new_product': {'delete_new_product': {'del_product': 'new_product'}},
                  'change_product_price': {'change_product_price': {'product': 'product', 'price': 'price'}},
                  'input_new_event': {'delete_event': {'event': 'event'}},
                  'change_event_name': {'change_event_name': {'event': 'event', 'name': 'name'}},
                  'change_event_date': {'change_event_date': {'month': 'month', 'day': 'day'}},
                  'input_event_product': {'delete_event_product': {'product': 'product'}}}


#undo dict list for forms.py
undo_dict_form = {'create_form_input_order': {'delete_form_input_order': {'event': 'event'}}}


class undo_func():

    def __init__(self, datafile: dict, undofile: dict, form_service = str, drive_service = str, folder_id = str):

        from functions import function_input
        from forms import function_forms

        self.datafile = datafile
        self.undofile = undofile
        self.func = function_input(datafile = datafile)
        
        self.form = function_forms(datafile = datafile,
                                   form_service = form_service,
                                   drive_service = drive_service,
                                   folder_id = folder_id
                                   )


    def output_data(self):

        dump_obj = json.dumps(self.datafile, indent = 4)

        with open("data.json", "w") as file:
            file.write(dump_obj)


    def output_undo(self):

        dump_obj = json.dumps(self.undofile, indent = 4)

        with open("undo.json", "w") as file:
            file.write(dump_obj)


    def redo(self):

        current_index = 0
        current_list = []

        for i in range(len(self.undofile)):
            indexa = list(self.undofile)[i]
            current_list.append(self.undofile[indexa][current])

        if current_list == []:
            return "There is nothing to redo."

        current_index = current_list.index(True)
        
        if current_index == 15:
            return "There is nothing to redo."
        elif current_index == 0 and len(self.undofile) == 1:
            return "There is nothing to redo."

        else:
            
            pre_index = list(self.undofile)[current_index] #timestamp of current action
            self.undofile[pre_index]['current'] = False
            
            current_index += 1 #need something to set the new spot as Current = True
            indexb = list(self.undofile)[current_index] #this is the timestamp of the upcoming index because redo
            self.undofile[indexb]['current'] = True
            
            types = self.undofile[indexb]['type']

            if types == 'func':
                
                undo_func = list(self.undofile[indexb])[0] #this is the function in the undofile
                inv_func = list(undo_dict_func[undo_func])[0] #finding the inverse of the function
                dicta = undo_dict_func[undo_func][inv_func] #params for inverse function
                output = ''

                for i in dicta:
                    
                    output = output + i + ' = ' + str(self.undofile[indexb][undo_func][dicta[i]]) + ', '

                value = f"self.func.{inv_func}({output})"

                exec(f"{value}")
                
                self.output_undo()
                self.output_data()
                return "All clear"

            elif types == 'form':

                undo_func = list(self.undofile[indexb])[0] #this is the function in the undofile
                inv_func = list(undo_dict_form[undo_func])[0] #finding the inverse of the function
                dicta = undo_dict_form[undo_func][inv_func] #params for inverse function
                output = ''

                for i in dicta:
                    
                    output = output + i + ' = ' + str(self.undofile[indexb][undo_func][dicta[i]]) + ', '

                value = f"self.form.{inv_func}({output})"

                exec(f"{value}")

                self.output_undo()
                self.output_data()
                return "All clear"
            


    def undo(self):

        current_index = 0
        current_list = []

        for i in range(len(self.undofile)):
            indexa = list(self.undofile)[i]
            current_list.append(self.undofile[indexa][current])

        if current_list == []:

            return "There is nothing to undo"

        current_index = current_list.index(True)

        if current_index == 0:

            return "There is nothing to undo"

        else:

            pre_index = list(self.undofile)[current_index] #timestamp of current action
            self.undofile[pre_index]['current'] = False
            
            current_index -= 1 #need something to set the new spot as Current = True
            indexb = list(self.undofile)[current_index] #this is the timestamp of the previous index because undo
            self.undofile[indexb]['current'] = True
            
            types = self.undofile[indexb]['type']

            if types == 'func':
                
                undo_func = list(self.undofile[indexb])[0] #this is the function in the undofile
                inv_func = list(undo_dict_func[undo_func])[0] #finding the inverse of the function
                dicta = undo_dict_func[undo_func][inv_func] #params for inverse function
                output = ''

                for i in dicta:
                    
                    output = output + i + ' = ' + str(self.undofile[indexb][undo_func][dicta[i]]) + ', '

                value = f"self.func.{inv_func}({output})"

                exec(f"{value}")
                
                self.output_undo()
                self.output_data()
                return "All clear"

            elif types == 'form':

                undo_func = list(self.undofile[indexb])[0] #this is the function in the undofile
                inv_func = list(undo_dict_form[undo_func])[0] #finding the inverse of the function
                dicta = undo_dict_form[undo_func][inv_func] #params for inverse function
                output = ''

                for i in dicta:
                    
                    output = output + i + ' = ' + str(self.undofile[indexb][undo_func][dicta[i]]) + ', '

                value = f"self.form.{inv_func}({output})"

                exec(f"{value}")

                self.output_undo()
                self.output_data()
                return "All clear"

        
class undo_input():


    def __init__(self):

        with open('undo.json', 'r') as undofiles:

            undofile = json.load(undofiles)

        self.undofile = undofile


    def output_undo(self):

        dump_obj = json.dumps(self.undofile, indent = 4)

        with open("undo.json", "w") as file:
            file.write(dump_obj)



    def new_action(self, action: str, param: dict, types: str):

        if len(self.undofile) == 15:
            index_firsta = list(self.undofile)[0]
            del self.undofile[index_firsta]

        for i in range(len(self.undofile)):
            indexi = list(self.undofile)[i]
            self.undofile[indexi]['current'] = False

        timestamp = str(int(time.time()))

        self.undofile[timestamp] = {}
        self.undofile[timestamp][action] = {}
        self.undofile[timestamp][action] = param
        self.undofile[timestamp]['current'] = True
        self.undofile[timestamp]['type'] = types

        self.output_undo()


        




