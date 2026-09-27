from datetime import datetime
from datetime import timedelta
from datetime import date
import datetime as dt

import json
import calendar
import time as t

import os
import json

from undo import undo_input


class function_input():

    def __init__(self, datafile: dict):

        self.datafile = datafile
        self.datetime = str(datetime.today().strftime('%Y/%m/%d'))
        self.func     = function_check(datafile = self.datafile)
        self.undo     = undo_input()


    def output_data(self):

        dump_obj = json.dumps(self.datafile, indent = 4)

        #with open("data.json", "w") as file:
        with open("data test for chart.json", "w") as file:
            file.write(dump_obj) 

    def input_cost(self, cost: float):

        undo_dicta = {'cost': cost}
        self.undo.new_action(action = 'input_cost', param = undo_dicta, types = 'func')
        
        self.datafile['YD_calendar'][self.datetime]['cost'] += cost
        self.datafile['YD_calendar'][self.datetime]['profit'] -= cost
        self.datafile['main_data']['cost'] += cost
        self.datafile['main_data']['profit'] -= cost
        self.func.refresh_cash_YD(amount = cost, cost = True, revenue = False)

        self.output_data()

        #return f"{cost} has been added to the data."


    def delete_cost(self, cost: float):

        #accidentally added the wrong cost
        if cost > self.datafile['main_data']['cost']:
            
            costa = self.datafile['main_data']['cost']
            return "You are reducing more cost than there is cost initially. Maximum amount that you can input is {costa}."

        self.datafile['YD_calendar'][self.datetime]['cost'] -= cost
        self.datafile['YD_calendar'][self.datetime]['profit'] += cost
        self.datafile['main_data']['cost'] -= cost
        self.datafile['main_data']['profit'] += cost
        self.func.refresh_cash_YD(amount = cost, cost = True, revenue = False)

        undo_dicta = {'cost': cost}
        self.undo.new_action(action = 'delete_cost', param = undo_dicta, types = 'func')

        self.output_data()

        return f"{cost} has been reduced from the data."
    

    def input_product_made(self, event: str, product: str, amount: int):

        product = product.lower()

        if event not in self.datafile['event']:
            return f"{event.title()} is not in list. Please add event to list."

        if product in self.datafile['product_pending']:
            special_occasion = False
        elif product in self.datafile['product_pending']['special_occasion']:
            special_occasion = True
        else:
            return f"{product.title()} not in list. Please add product to list."
                  
        if special_occasion == False:
            self.datafile['product_pending'][product] += amount
        elif special_occasion == True:  
            self.datafile['product_pending']['special_occasion'][product] += amount

        undo_dicta = {'event': event, 'product': product, 'amount': amount}
        #self.undo.new_action(action = 'input_product_made', param = undo_dicta, types = 'func')        
        
        self.func.refresh_orders_tofill()
        self.output_data()

        #return f"{product.title()} has been added to the data structure for {event}."


    def delete_product_made(self, event: str, product: str, amount: int):
        
        product = product.lower()

        if event not in self.datafile['event']:
            return f"{event.title()} is not in list. Please add event to list."

        if product in self.datafile['product_pending']:
            special_occasion = False
        elif product in self.datafile['product_pending']['special_occasion']:
            special_occasion = True
        else:
            return f"{product.title()} is not even in the list. There is nothing to delete"
        
        if special_occasion == False:
            if amount > self.datafile['product_pending'][product]:
                amounta = self.datafile['product_pending'][product]
                return f"There is only {amounta} {product} in reserve, you cannot delete more than {amounta} of {product} from the reserve."
            else: 
                self.datafile['product_pending'][product] -= amount
        elif special_occasion == True:
            if amount > self.datafile['product_pending']['special_occasion'][product]:
                amounta = self.datafile['product_pending']['special_occasion'][product]
                return f"There is only {amounta} {product} in reserve, you cannot delete more than {amounta} of {product} from the reserve."
            else:
                self.datafile['product_pending']['special_occasion'][product] -= amount

        undo_dicta = {'event': event, 'product': product, 'amount': amount}
        self.undo.new_action(action = 'delete_product_made', param = undo_dicta, types = 'func')
            
        self.func.refresh_orders_tofill()
        self.output_data()

        return f"{product.title()} has been removed from the data structure for {event}."


    def input_product_pending(self, event: str, product: str, amount: int, cost: float):

        undo_dicta = {'event': event, 'product': product, 'amount': amount, 'cost': cost}
        self.undo.new_action(action = 'input_product_pending', param = undo_dicta, types = 'func')

        cost = self.input_cost(cost = cost)
        product_made = self.input_product_made(event = event, product = product, amount = amount)

        return cost, product_made


    def delete_product_pending(self, event: str, product: str, amount: int, cost: float):

        undo_dicta = {'event': event, 'product': product, 'amount': amount, 'cost': cost}
        self.undo.new_action(action = 'delete_product_pending', param = undo_dicta, types = 'func')

        cost = self.delete_cost(cost = cost)
        product_made = self.delete_product_made(event = event, product = product, amount = amount)

        return cost, product_made
        
        
    def input_time_spent(self, hour: int, minute: int):

        undo_dicta = {'hour': hour, 'minute': minute}
        self.undo.new_action(action = 'input_time_spent', param = undo_dicta, types = 'func')

        hours = hour + ( int(minute/60) )
        minutes = minute % 60

        self.datafile['YD_calendar'][self.datetime]['time_spent']['hour'] += hours
        self.datafile['YD_calendar'][self.datetime]['time_spent']['minute'] += minutes
        self.datafile['main_data']['time_spent']['hour'] += hours
        self.datafile['main_data']['time_spent']['minute'] += minutes
        self.func.refresh_YD_time(hour = hours, minute = minutes)

        self.output_data()
        return f"{hours} hours and {minutes} minutes has been added to the data."
        

    def delete_time_spent(self, hour: int, minute: int):

        undo_dicta = {'hour': hour, 'minute': minute}
        self.undo.new_action(action = 'delete_time_spent', param = undo_dicta, types = 'func')

        hours = hour + ( int(minute/60) )
        minutes = minute % 60

        self.datafile['YD_calendar'][self.datetime]['time_spent']['hour'] -= hours
        self.datafile['YD_calendar'][self.datetime]['time_spent']['minute'] -= minutes
        self.datafile['main_data']['time_spent']['hour'] -= hours
        self.datafile['main_data']['time_spent']['minute'] -= minutes
        self.func.refresh_YD_time(hour = hours, minute = minutes)

        self.output_data()
        return f"{hours} hours and {minutes} minutes has been removes from the data."
        

    def input_product_sold(self, event: str, amount: int, product: str, special_occasion: bool):
        
        #note that object have to calculate the cost prehand

        product = product.lower()

        #price_product = self.datafile['type_of_products']
        
        if special_occasion == True:
            product_price = float(self.datafile['type_of_products']['special_occasion'][product])
            cost = amount * product_price
        elif special_occasion == False:
            product_price = float(self.datafile['type_of_products'][product])
            cost = amount * product_price

        if special_occasion == False:
            self.datafile['product_pending'][product] -= amount
            if product in self.datafile['product_sold']:                    
                self.datafile['product_sold'][product] += amount
            else:
                self.datafile['product_sold'][product] = amount
            if product in self.datafile['YD_calendar'][self.datetime]['product_sold']:
                self.datafile['YD_calendar'][self.datetime]['product_sold'][product] += amount
            else:
                self.datafile['YD_calendar'][self.datetime]['product_sold'][product] = amount
            self.datafile['main_data']['revenue'] += cost
            self.datafile['main_data']['profit'] += cost
            self.datafile['YD_calendar'][self.datetime]['revenue'] += cost
            self.datafile['YD_calendar'][self.datetime]['profit'] += cost
            self.func.refresh_cash_YD(amount = cost, cost = False, revenue = True)
            
        elif special_occasion == True:
            self.datafile['product_pending']['special_occasion'][product] -= amount
            if product in self.datafile['product_sold']['special_occasion']:                    
                self.datafile['product_sold']['special_occasion'][product] += amount
            else:
                self.datafile['product_sold']['special_occasion'][product] = amount
            if product in self.datafile['YD_calendar'][self.datetime]['product_sold']['special_occasion']:
                self.datafile['YD_calendar'][self.datetime]['product_sold']['special_occasion'][product] += amount
            else:
                self.datafile['YD_calendar'][self.datetime]['product_sold']['special_occasion'][product] = amount
            self.datafile['main_data']['revenue'] += cost
            self.datafile['main_data']['profit'] += cost
            self.datafile['YD_calendar'][self.datetime]['revenue'] += cost
            self.datafile['YD_calendar'][self.datetime]['profit'] += cost
            self.func.refresh_cash_YD(amount = cost, cost = False, revenue = True)
            
        self.func.refresh_YD_product(product = product, amount = amount, special_occasion = special_occasion)
        self.output_data()
        

    def input_new_product(self, new_product: str, special_occasion: bool, price: float):

        new_product = new_product.lower()
        if new_product in self.datafile['type_of_products'] or new_product in self.datafile['type_of_products']['special_occasion']:
            return f"{new_product.title()} is already in the 'type of product' list."
        
        undo_dicta = {'new_product': new_product, 'special_occasion': special_occasion, 'price': price}
        self.undo.new_action(action = 'input_new_product', param = undo_dicta, types = 'func')
        
        if special_occasion == False:
            self.datafile['type_of_products'][new_product] = price
        else:
            self.datafile['type_of_products']['special_occasion'][new_product] = price

        self.output_data()
        return f"{new_product.title()} is added into the 'type of product' list."


    def delete_new_product(self, del_product: str):

        del_product = del_product.lower()
        if del_product not in self.datafile['type_of_products'] or del_product not in self.datafile['type_of_products']['special_occasion']:
            return f"{del_product.title()} is not in the 'type of product' list. Please enter a product that is in the 'type of product' list."

        price = self.datafile['type_of_products'][del_product]

        if del_product in self.datafile['type_of_products']:
            special_occasion = False
        elif del_product in self.datafile['type_of_products']['special_occasion']:
            special_occasion = True

        undo_dicta = {'del_product': del_product, 'special_occasion': special_occasion, 'price': price}
        self.undo.new_action(action = 'delete_new_product', param = undo_dicta, types = 'func')
        
        if special_occasion == False:
            del self.datafile['type_of_products'][del_product] 
        else:
            del self.datafile['type_of_products']['special_occasion'][del_product]

        self.output_data()
        return f"{del_product.title()} has been deleted from the 'type of product' list."
    

    def input_orders(self, name: str, event: str, product: str, amount: int):

        undo_dicta = {'name': name, 'event': event, 'product': product, 'amount': amount}
        self.undo.new_action(action = 'input_orders', param = undo_dicta, types = 'func')

        product = product.lower()

        if product in self.datafile['orders_tofill'][event]:
            special_occasion = False
        elif product in self.datafile['orders_tofill'][event]['special_occasion']:
            special_occasion = True

        if name in self.datafile['manual_orders_req_cancellation'][event] == False:
            self.datafile['manual_orders_req_cancellation'][event][name] = { 'special_occasion':{} }
        
        if special_occasion == False:
            if product in self.datafile['manual_orders_req_cancellation'][event][name]:
                self.datafile['manual_orders_req_cancellation'][event][name][product] += amount
            else:
                self.datafile['manual_orders_req_cancellation'][event][name][product] = amount
        if special_occasion == True:
            if product in self.datafile['manual_orders_req_cancellation'][event][name]['special_occasion']:
                self.datafile['manual_orders_req_cancellation'][event][name]['special_occasion'][product] += amount
            else:
                self.datafile['manual_orders_req_cancellation'][event][name]['special_occasion'][product] = amount

        self.func.check_all()
        self.output_data()

        return f"{amount} {product} has been added for {name} for the event '{event}'."


    def delete_orders(self, name: str, event: str, product: str, amount: int):

        product = product.lower()

        if product in self.datafile['orders_tofill'][event]:
            special_occasion = False
        elif product in self.datafile['orders_tofill'][event]['special_occasion']:
            special_occasion = True
        
        if special_occasion == False:
            if amount > self.datafile['manual_orders_req_cancellation'][event][name][product]:
                amounta = self.datafile['manual_orders_req_cancellation'][event][name][product]
                return f"Error. You are deleting {amount} {product}, when {name} only ordered {amounta} {product}."
            elif amount == self.datafile['manual_orders_req_cancellation'][event][name][product]:
                del self.datafile['manual_orders_req_cancellation'][event][name][product]
            else:
                self.datafile['manual_orders_req_cancellation'][event][name][product] -= amount
        if special_occasion == True:
            if amount > self.datafile['manual_orders_req_cancellation'][event][name]['special_occasion'][product]:
                amounta = self.datafile['manual_orders_req_cancellation'][event][name]['special_occasion'][product]
                return f"Error. You are deleting {amount} {product}, when {name} only ordered {amounta} {product}."
            elif amount == self.datafile['manual_orders_req_cancellation'][event][name]['special_occasion'][product]:
                del self.datafile['manual_orders_req_cancellation'][event][name]['special_occasion'][product]
            else:
                self.datafile['manual_orders_req_cancellation'][event][name]['special_occasion'][product] -= amount

        undo_dicta = {'name': name, 'event': event, 'product': product, 'amount': amount}
        self.undo.new_action(action = 'delete_orders', param = undo_dicta, types = 'func')
                
        self.func.check_all()
        self.output_data()

        return f"{amount} {product} has been removed for {name}'s order for the event '{event}'."


    def input_new_event(self, event: str, name: str):

        undo_dicta = {'event': event}
        self.undo.new_action(action = 'input_new_event', param = undo_dicta, types = 'func')

        self.datafile['event'].append(event)         
        #self.datafile['product_pending'][event] = {'special_occasion': {}} 
        self.datafile['orders_tofill'][event] = {'special_occasion': {}}
        self.datafile['orders_req_cancellation'][event] = {}
        self.datafile['manual_orders_req_cancellation'][event] = {}
        self.datafile['form_id'][event] = {'input': '',
                                           'output': ''}
        self.datafile['event_name'][event] = name.title()

        self.output_data()
        
        return f"{name.title()} has been created."


    def change_event_name(self, event: str, name: str):

        prename = self.datafile['event_name'][event]

        undo_dicta = {'event': event, 'name': prename}
        self.undo.new_action(action = 'change_event_name', param = undo_dicta, types = 'func')
            
        self.datafile['event_name'][event] = name.title()

        return f"The name of the event {prename.title()}, has been changed to {name.title()}."


    def delete_event(self, event: str):

        self.datafile['event'].remove(event)         
        #del self.datafile['product_pending'][event] 
        del self.datafile['orders_tofill'][event] 
        del self.datafile['orders_req_cancellation'][event]
        del self.datafile['manual_orders_req_cancellation'][event]
        del self.datafile['form_id'][event]
        del self.datafile['event_name'][event]

        '''function form delete forms'''

        self.output_data()
        
        return f"{name.title()} has been created."

    '''def discard_product(self, event: str, product: str, amount: int, special_occasion: bool, ifall: bool):

        #this function is only used after product is already made and is going to go to waste.
        #will be a button for the user to throw out this object
        #only available once date of event has passed

        end = int(datetime.strptime(event, '%Y/%m/%d').timestamp())
        now = int(t.time())
        product = product.lower()

        if now > event:

            del self.datafile['form_id'][event]

            if special_occasion == False:

                if ifall == False:

                    if product not in self.datafile['YD_calendar'][self.datetime]['net_loss']:
                
                        self.datafile['YD_calendar'][self.datetime]['net_loss'][product] = 0
                        self.datafile['YD_calendar'][self.datetime]['net_loss'][product] += amount

                    else:

                        self.datafile['YD_calendar'][self.datetime]['net_loss'][product] += amount

                    self.datafile['product_pending'][product] -= amount
                    self.datafile['net_loss'][event][product] += amount
            

                if ifall == True:

                    if product not in self.datafile['YD_calendar'][self.datetime]['net_loss']:
                
                        self.datafile['YD_calendar'][self.datetime]['net_loss'][product] = self.datafile['product_pending'][product]

                    else:

                        self.datafile['YD_calendar'][self.datetime]['net_loss'][product] += self.datafile['product_pending'][product]
                       
                    self.datafile['net_loss'][event][product] += self.datafile['product_pending'][product]
                    self.datafile['product_pending'][product] = 0

                if ifall == False:
                    self.func.refresh_YD_net_loss(product = product, amount = amount, special_occasion = special_occasion)
                else:
                    self.func.refresh_YD_net_loss(product = product, amount = self.datafile['product_pending'][product], special_occasion = special_occasion)

            else:

                if ifall == False:

                    if product not in self.datafile['YD_calendar'][self.datetime]['net_loss']['special_occasion']:
                
                        self.datafile['YD_calendar'][self.datetime]['net_loss']['special_occasion'][product] = amount

                    else:

                        self.datafile['YD_calendar'][self.datetime]['net_loss']['special_occasion'][product] += amount

                    self.datafile['product_pending']['special_occasion'][product] -= amount
                    self.datafile['net_loss'][event]['special_occasion'][product] += amount

                if ifall == True:

                    if product not in self.datafile['YD_calendar'][self.datetime]['net_loss']['special_occasion']:
                
                        self.datafile['YD_calendar'][self.datetime]['net_loss']['special_occasion'][product] = self.datafile['product_pending']['special_occasion'][product]

                    else:

                        self.datafile['YD_calendar'][self.datetime]['net_loss']['special_occasion'][product] += self.datafile['product_pending']['special_occasion'][product]

                    self.datafile['product_pending']['special_occasion'][product] = 0
                    self.datafile['net_loss'][event]['special_occasion'][product] += self.datafile['product_pending'][product]

                if ifall == False:
                    self.func.refresh_YD_net_loss(product = product, amount = amount, special_occasion = special_occasion)
                else:
                    self.func.refresh_YD_net_loss(product = product, amount = self.datafile['product_pending']['special_occasion'][product], special_occasion = special_occasion)


        else:

            return "Event hasnt passed"
        

        self.output_data()'''


    def input_event_product(self, event: str, product: str):
        #this is to input in products that will be within the specific event.
        event_name = self.datafile['event_name'][event]
        
        if product in self.datafile['type_of_products']:

            if product in self.datafile['orders_tofill'][event]:
                return f"{product.title()} is already in the {event_name}."
            else:
                self.datafile['orders_tofill'][event][product] = 0
                self.datafile['product_pending'][product] = 0
                return f"{product.title()} has been successfully added to the list for {event_name}."
            
        elif product in self.datafile['type_of_products']['special_occasion']:

            if product in self.datafile['orders_tofill']['special_occasion'][event]:
                return f"{product.title()} is already in the {event_name}."
            else:
                self.datafile['orders_tofill'][event]['special_occasion'][product] = 0
                self.datafile['product_pending']['special_occasion'][product] = 0
                return f"{product.title()} has been successfully added to the list for {event_name}."
            
        else:
            return "Product not in list."

        undo_dicta = {'event': event, 'product': product}
        self.undo.new_action(action = 'input_event_product', param = undo_dicta, types = 'func')

        self.output_data()


    def delete_event_product(self, event: str, product: str):
        #this is to input in products that will be within the specific event.
        event_name = self.datafile['event_name'][event]
        
        if product in self.datafile['type_of_products']:

            if product not in self.datafile['orders_tofill'][event]:
                return f"{product.title()} is not even in the list for {event_name}."
            else:
                del self.datafile['orders_tofill'][event][product] 
                #del self.datafile['product_pending'][event][product] 
                return f"{product.title()} has been successfully removed from the list for {event_name}."
            
        elif product in self.datafile['type_of_products']['special_occasion']:

            if product not in self.datafile['orders_tofill']['special_occasion'][event]:
                return f"{product.title()} is not even in the in the {event_name}."
            else:
                del self.datafile['orders_tofill'][event]['special_occasion'][product] 
                #del self.datafile['product_pending'][event]['special_occasion'][product] 
                return f"{product.title()} has been successfully removed from the list for {event_name}."

        self.output_data()
        


class function_check():
    

    def __init__(self, datafile: dict):

        self.datafile = datafile
        self.year = str(datetime.today().strftime('%Y'))
        self.datetime = str(datetime.today().strftime('%Y/%m/%d'))
        

    def output_data(self):

        dump_obj = json.dumps(self.datafile, indent = 4)

        with open("data.json", "w") as file:
            file.write(dump_obj)



    def refresh_YD_time(self, hour: int, minute: int):

        self.datafile['main_data']['time_spent_YD']['hour'] += hour
        self.datafile['main_data']['time_spent_YD']['minute'] += minute

        self.output_data()


    def refresh_YD_product(self, product: str, amount: int, special_occasion: bool):

        product = product.lower()
        if special_occasion == False:
            if product in self.datafile['product_sold_YD']:
                self.datafile['product_sold_YD'][product] += amount
            else:
                self.datafile['product_sold_YD'][product] = amount
        else:
            if product in self.datafile['product_sold_YD']['special_occasion']:
                self.datafile['product_sold_YD']['special_occasion'][product] += amount
            else:
                self.datafile['product_sold_YD']['special_occasion'][product] = amount
            self.output_data()


    def refresh_YD_net_loss(self, product: str, amount: int, special_occasion: bool):

        product = product.lower()
        
        if special_occasion == False:
            if product in list(self.datafile['net_loss_YD']):
                self.datafile['net_loss_YD'][product] += amount
            else:
                self.datafile['net_loss_YD'][product] = amount
        else:
            if product in list(self.datafile['net_loss_YD']['special_occasion']):
                self.datafile['net_loss_YD']['special_occasion'][product] += amount
            else:
                self.datafile['net_loss_YD']['special_occasion'][product] = amount

        self.output_data()
                
            
    def refresh_cash_YD(self, amount: float, cost = False, revenue = False):

        if revenue == True:
            self.datafile['main_data']['revenue_YD'] += amount
        if cost == True:
            self.datafile['main_data']['cost_YD'] += amount
        self.datafile['main_data']['profit_YD'] = self.datafile['main_data']['revenue_YD'] - self.datafile['main_data']['cost_YD']

        self.output_data()
        

    def refresh_YD_data(self):

        revenue_YD = 0
        cost_YD = 0
        profit_YD = 0
        time_spent_YD = {'hour': 0, 'minute': 0}
        hours = 0
        minutes = 0
        self.datafile['product_sold_YD'] = { 'special_occasion': {} }
        self.datafile['net_loss_YD'] = { 'special_occasion': {} }

        for i in range(len(list(self.datafile['YD_calendar']))):
            revenue_YD += self.datafile['YD_calendar'][str(list(self.datafile['YD_calendar'])[i])]['revenue']
            cost_YD += self.datafile['YD_calendar'][str(list(self.datafile['YD_calendar'])[i])]['cost']
            profit_YD += self.datafile['YD_calendar'][str(list(self.datafile['YD_calendar'])[i])]['profit']
            hours += self.datafile['YD_calendar'][str(list(self.datafile['YD_calendar'])[i])]['time_spent']['hour']
            minutes += self.datafile['YD_calendar'][str(list(self.datafile['YD_calendar'])[i])]['time_spent']['minute']

        
            for j in list(self.datafile['YD_calendar'][list(self.datafile['YD_calendar'])[i]]['product_sold']):
                if j not in self.datafile['product_sold_YD']:
                    self.datafile['product_sold_YD'][j] = self.datafile['YD_calendar'][list(self.datafile['YD_calendar'])[i]]['product_sold'][j]
                elif j in self.datafile['product_sold_YD'] and j != 'special_occasion':
                    self.datafile['product_sold_YD'][j] += self.datafile['YD_calendar'][list(self.datafile['YD_calendar'])[i]]['product_sold'][j]

            for k in list(self.datafile['YD_calendar'][list(self.datafile['YD_calendar'])[i]]['product_sold']['special_occasion']):
                if k not in self.datafile['product_sold_YD']['special_occasion']:
                    self.datafile['product_sold_YD']['special_occasion'][k] = self.datafile['YD_calendar'][list(self.datafile['YD_calendar'])[i]]['product_sold']['special_occasion'][k]
                else:
                    self.datafile['product_sold_YD']['special_occasion'][k] += self.datafile['YD_calendar'][list(self.datafile['YD_calendar'])[i]]['product_sold']['special_occasion'][k]
                    
            for j in list(self.datafile['YD_calendar'][list(self.datafile['YD_calendar'])[i]]['net_loss']):
                if j not in self.datafile['net_loss_YD']:
                    self.datafile['net_loss_YD'][j] = self.datafile['YD_calendar'][list(self.datafile['YD_calendar'])[i]]['product_sold'][j]
                elif j in self.datafile['net_loss_YD'] and j != 'special_occasion':
                    self.datafile['net_loss_YD'][j] += self.datafile['YD_calendar'][list(self.datafile['YD_calendar'])[i]]['product_sold'][j]

            for k in list(self.datafile['YD_calendar'][list(self.datafile['YD_calendar'])[i]]['net_loss']['special_occasion']):
                if k not in self.datafile['net_loss_YD']['special_occasion']:
                    self.datafile['net_loss_YD']['special_occasion'][k] = self.datafile['YD_calendar'][list(self.datafile['YD_calendar'])[i]]['net_loss']['special_occasion'][k]
                else:
                    self.datafile['net_loss_YD']['special_occasion'][k] += self.datafile['YD_calendar'][list(self.datafile['YD_calendar'])[i]]['net_loss']['special_occasion'][k]
                    
        time_spent_YD['hour'] = hours + ( int(minutes/60) )
        time_spent_YD['minute'] = minutes % 60

        self.datafile['main_data']['revenue_YD'] = revenue_YD
        self.datafile['main_data']['cost_YD'] = cost_YD
        self.datafile['main_data']['profit_YD'] = profit_YD
        self.datafile['main_data']['time_spent_YD'] = time_spent_YD

        self.datafile['main_data']['profit_YD'] = self.datafile['main_data']['revenue_YD'] - self.datafile['main_data']['cost_YD']

        #revenue_YD, cost_YD, profit_YD, time_spent_YD, product_sold_YD, net_loss_YD

        self.output_data()


    def check_YD_calendar(self):
        #to add 365 days in the calendar
        #self.datafile['YD_calendar'][self.datetime] = {'revenue': 0, 'cost': 0, 'profit': 0, 'time_spent': 0, 'product_sold': {}}

        if bool(self.datafile['YD_calendar']) ==  False:
            start = datetime(int(self.year), 1, 1, 0, 0, 0)
            end = datetime(int(self.year), 12, 31, 0, 0, 0)
            delta = end - start
            for i in range(delta.days + 1):
                self.datafile['YD_calendar'][(start + timedelta(days = i)).strftime('%Y/%m/%d')] = {'revenue': 0,
                                                                                                    'cost': 0,
                                                                                                    'profit': 0,
                                                                                                    'time_spent': {'hour': 0, 'minute': 0},
                                                                                                    'product_sold': {'special_occasion': {}},
                                                                                                    'net_loss': {'special_occasion': {}}
                                                                                                    }
        else:
            year_of_datafile = list(self.datafile['YD_calendar'])[0][:4]
            start = datetime(int(self.year), 1, 1, 0, 0, 0)
            end = datetime(int(self.year), 12, 31, 0, 0, 0)
            delta = end - start
            if year_of_datafile != self.year:
                for i in range(delta.days + 1):            
                    self.datafile['YD_calendar'][(start + timedelta(days=i)).strftime('%Y/%m/%d')] = {'revenue': 0,
                                                                                                      'cost': 0,
                                                                                                      'profit': 0,
                                                                                                      'time_spent': {'hour': 0, 'minute': 0},
                                                                                                      'product_sold': {'special_occasion': {}},
                                                                                                      'net_loss': {'special_occasion': {}}
                                                                                                      }
        self.output_data()          


    def check_event_remove(self):

        for i in range(len(self.datafile['event'])):
            end = int(datetime.strptime((date.today().year + '/' + self.datafile['event'][i]), '%Y/%m/%d').timestamp())
            now = int(t.time())
            endplus = end + 432000 #expiration date + 5 day. 432 000 is 5 days in seconds
            if now > end and endplus > now: #if expiration is reached but still within 5 days
                self.display.display_warning_list(event = self.datafile['event'][i])
            elif now > endplus: #if expiration is reached but after 5 days
                for product in list(self.datafile['product_pending'][self.datafile['event'][i]]):
                    if product != 'special_occasion':
                        if product in self.datafile['net_loss']:
                            self.datafile['net_loss'][product] += self.datafile['product_pending'][self.datafile['event'][i]][product]
                        else:
                            self.datafile['net_loss'][product] = self.datafile['product_pending'][self.datafile['event'][i]][product]
                        if product in self.datafile['YD_calendar'][self.datetime]['net_loss']:
                            self.datafile['YD_calendar'][self.datetime]['net_loss'][product] += self.datafile['product_pending'][self.datafile['event'][i]][product]
                        else:
                            self.datafile['YD_calendar'][self.datetime]['net_loss'][product] = self.datafile['product_pending'][self.datafile['event'][i]][product]
                        self.refresh_YD_net_loss(product = product,
                                                 amount = self.datafile['product_pending'][self.datafile['event'][i]][product],
                                                 special_occasion = True)
                    elif product == 'special_occasion':
                        for product_s in list(self.datafile['product_pending'][self.datafile['event'][i]]['special_occasion']):
                            if product_s in self.datafile['net_loss']['special_occasion']:
                                self.datafile['net_loss']['special_occasion'][product_s] += self.datafile['product_pending'][self.datafile['event'][i]]['special_occasion'][product_s]
                            else:
                                self.datafile['net_loss']['special_occasion'][product_s] = self.datafile['product_pending'][self.datafile['event'][i]]['special_occasion'][product_s]
                            if product_s in self.datafile['YD_calendar'][self.datetime]['net_loss']['special_occasion']:
                                self.datafile['YD_calendar'][self.datetime]['net_loss']['special_occasion'][product_s] += self.datafile['product_pending'][self.datafile['event'][i]]['special_occasion'][product_s]
                            else:
                                self.datafile['YD_calendar'][self.datetime]['net_loss']['special_occasion'][product_s] = self.datafile['product_pending'][self.datafile['event'][i]]['special_occasion'][product_s]   
                            self.refresh_YD_net_loss(product = product_s,
                                                     amount = self.datafile['product_pending'][self.datafile['event'][i]]['special_occasion'][product_s],
                                                     special_occasion = True)
                            
                #del self.datafile['product_pending'][self.datafile['event'][i]]
                del self.datafile['orders_tofill'][self.datafile['event'][i]]
                del self.datafile['event_name'][self.datafile['event'][i]]
                del self.datafile['orders_req_cancellation'][self.datafile['event'][i]]
                del self.datafile['manual_orders_req_cancellation'][self.datafile['event'][i]]
                self.datafile['event'].remove(self.datafile['event'][i])
    
            elif now > end and self.datafile['product_pending'][self.datafile['event'][i]] == {'special_occasion': {} }:

                #del self.datafile['product_pending'][self.datafile['event'][i]]
                del self.datafile['orders_tofill'][self.datafile['event'][i]]
                del self.datafile['event_name'][self.datafile['event'][i]]
                del self.datafile['orders_req_cancellation'][self.datafile['event'][i]]
                del self.datafile['manual_orders_req_cancellation'][self.datafile['event'][i]]
                self.datafile['event'].remove(self.datafile['event'][i])
               
        self.output_data()


    def refresh_orders_tofill(self):

        dict_pending = {}

        #creating the dictionary of dict_pending
        for i in range(len(list(self.datafile['orders_tofill']))):
            event_name = list(self.datafile['orders_tofill'])[i]
            dict_pending[event_name] = {}
            for j in range(len(list(self.datafile['orders_tofill'][event_name]))):
                product_name = list(self.datafile['orders_tofill'][event_name])[j]
                if product_name != 'special_occasion':
                    dict_pending[event_name][product_name] = 0
                else:
                    dict_pending[event_name]['special_occasion'] = {}
                    for k in range(len(list(self.datafile['orders_tofill'][event_name]['special_occasion']))):       
                        special_occa_product_name = list(self.datafile['orders_tofill'][event_name]['special_occasion'])[k]
                        dict_pending[event_name]['special_occasion'][special_occa_product_name] = 0
        
        for i in range(len(list(self.datafile['orders_req_cancellation']))):
            event_name = list(self.datafile['orders_req_cancellation'])[i]
            for j in range(len(list(self.datafile['orders_req_cancellation'][event_name]))):
                name = list(self.datafile['orders_req_cancellation'][event_name])[j]
                for k in range(len(list(self.datafile['orders_req_cancellation'][event_name][name]))):
                    product = list(self.datafile['orders_req_cancellation'][event_name][name])[k]
                    if product in list(dict_pending[event_name]):      
                        dict_pending[event_name][product] += self.datafile['orders_req_cancellation'][event_name][name][product]
                    else:
                        dict_pending[event_name]['special_occasion'][product] += self.datafile['orders_req_cancellation'][event_name][name][product]
                        
        for i in range(len(list(self.datafile['product_pending']))):
            event_name = list(self.datafile['product_pending'])[i]
            for j in range(len(list(self.datafile['product_pending']))):
                product_name = list(self.datafile['product_pending'])[j]
                if product_name != 'special_occasion':
                    dict_pending[event_name][product] -= self.datafile['product_pending'][product_name]
                else:
                    dict_pending[event_name]['special_occasion'][product] -= self.datafile['product_pending']['special_occasion'][product_name]

        self.datafile['orders_tofill'] = dict_pending
        self.output_data()

    def orders_req_refresh(self):

        for i in range(len(self.datafile['manual_orders_req_cancellation'])):
            event = list(self.datafile['manual_orders_req_cancellation'])[i]
            lena = len(self.datafile['manual_orders_req_cancellation'][event])
            for j in range(lena):
                product_name = list(self.datafile['manual_orders_req_cancellation'][event])[j]
                self.datafile['orders_req_cancellation'][event][product_name] += self.datafile['manual_orders_req_cancellation'][event][product_name]

        self.output_data()


    def check_all(self):

        self.check_YD_calendar()
        self.refresh_YD_data()
        self.check_event_remove()
        self.orders_req_refresh()
        self.refresh_orders_tofill()


def data_retrieve(drive_service: str, folder_id: str):

    import io
    from googleapiclient.http import MediaIoBaseDownload
    from googleapiclient.http import MediaFileUpload

    '''
    path = 'data.json'

    if os.path.exists(path):

        with open("data.json", "r") as datafile:
            data = json.load(datafile)
            
    else:
        
        from default import new_main_dict

        dump_obj = json.dumps(new_main_dict, indent = 4)

        with open("data.json", "w") as datafile:
            datafile.write(dump_obj)

        with open("data.json", "r") as datafile:
            data = json.load(datafile)
    '''

    query = f"parents = '{folder_id}'"
    
    results = drive_service.files().list(
        q = query,
        fields  = "nextPageToken, files(id, name)").execute()

    filenames = []
    
    for i in range(len(results['files'])):
        file_name = results['files'][i]['name']
        filenames.append(file_name)

    if 'data.json' in filenames: #if data.json file exist in folder, retrieve the data
        
        #retrieving fileId
        index = filenames.index('data.json')
        data_fileId = results['files'][index]['id']

        #retrieving data
        result = drive_service.files().get_media(
            fileId   = data_fileId
            )
        
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, result)
        done = False

        while done is False:
            status, done = downloader.next_chunk()
            
        fh.seek(0)

        data = json.loads(fh.read().decode("utf-8"))
        
        #saving data into data.json file            
        dump_obj = json.dumps(data, indent = 4)

        with open("data.json", "w") as datafile:
            datafile.write(dump_obj)


    else: #if data.json file does not exist in folder, create the file and retreive the data

        path = 'data.json'

        if os.path.exists(path):

            with open("data.json", "r") as datafile:
                data = json.load(datafile)
                
        else:
            
            from default import new_main_dict

            dump_obj = json.dumps(new_main_dict, indent = 4)

            with open("data.json", "w") as datafile:
                datafile.write(dump_obj)

            with open("data.json", "r") as datafile:
                data = json.load(datafile)

        folder_id = folder_id
        file_name = 'data.json'

        file_metadata = {
            'name': file_name,
            'parents': [folder_id],
            }

        media = MediaFileUpload(file_name, mimetype = 'text/plain')
        
        #creating a brand new file
        data_fileId = drive_service.files().create(
            body = file_metadata,
            media_body = media,
            fields='id'
            ).execute()['id']


    return data, data_fileId


def data_save(drive_service: str, data_fileId: str, folder_id: str):

    from googleapiclient.http import MediaFileUpload

    folder_id = folder_id
    file_name = 'data.json'

    file_metadata = {
        'name': 'data.json',
        'parents': [folder_id],
        }

    media = MediaFileUpload(file_name, mimetype = 'text/plain')

    #replacing the data of a file
    drive_service.files().update(
        fileId = data_fileId,
        media_body = media
        ).execute()


def drive_check(drive_service: str):

    #check if storage folder exists within drive and returns the folderid
    response = drive_service.files().list(
        q="name='Data_storage_for_bakesale_app-DO_NOT_DELETE' and mimeType='application/vnd.google-apps.folder'",
    ).execute()

    if response['files'] == []: #does not exist
        
        file_metadata = {
            'name': 'Data_storage_for_bakesale_app-DO_NOT_DELETE',
            'mimeType': 'application/vnd.google-apps.folder',
            }

        folder_id = drive_service.files().create(body = file_metadata).execute()['id']
        return folder_id
    
    else: #exists
        
        folder_id = response['files'][0]['id']
        return folder_id

    #if storage folder does NOT exist, create storage folder and data.json


def undo_init():

    dicta = {}
   
    dump_obj = json.dumps(dicta, indent = 4)

    with open("undo.json", "w") as datafile:
        datafile.write(dump_obj)

    return dicta
    

def connection_check():

    import socket


    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False
        



    






























    

    
