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
        with open("data.json", "w") as file:
            file.write(dump_obj) 

    def input_cost(self, cost: float):

        self.datafile['YD_calendar'][self.datetime]['cost'] += cost
        self.datafile['YD_calendar'][self.datetime]['profit'] -= cost
        self.datafile['main_data']['cost'] += cost
        self.datafile['main_data']['profit'] -= cost

        #undo-redo
        undo_dicta = {'cost': cost}
        self.undo.new_action(action = 'input_cost', param = undo_dicta, types = 'func')

        self.output_data()
        self.func.refresh_YD_cost(date = self.datetime, cost = cost)
        self.func.refresh_YD_product()

        return "All clear"


    def delete_cost(self, cost: float):

        #accidentally added the wrong cost
        if cost > self.datafile['main_data']['cost']:
            costa = self.datafile['main_data']['cost']
            return "You are reducing more cost than there is cost initially. Maximum amount that you can input is {costa}."

        self.datafile['YD_calendar'][self.datetime]['cost'] -= cost
        self.datafile['YD_calendar'][self.datetime]['profit'] += cost
        self.datafile['main_data']['cost'] -= cost
        self.datafile['main_data']['profit'] += cost

        #undo-redo
        undo_dicta = {'cost': cost}
        self.undo.new_action(action = 'delete_cost', param = undo_dicta, types = 'func')

        self.output_data()
        self.func.refresh_YD_cost(date = self.datetime, cost = -cost)
        self.func.refresh_YD_product()

        return f"{cost} has been reduced from the data."
    

    def input_product_made(self, product: str, amount: int):

        product = product.lower()
        event = self.datafile['event'][0]

        if product in self.datafile['orders_tofill'][event]:
            special_occasion = False
        elif product in self.datafile['orders_tofill'][event]['special_occasion']:
            special_occasion = True

        if amount != 0:
            if special_occasion == False:
                if product not in self.datafile['product_pending']:
                    self.datafile['product_pending'][product] = 0
                self.datafile['product_pending'][product] += amount
            elif special_occasion == True:
                if product not in self.datafile['product_pending']['special_occasion']:
                    self.datafile['product_pending']['special_occasion'][product] = 0
                self.datafile['product_pending']['special_occasion'][product] += amount

        #undo-redo
        undo_dicta = {'product': product, 'amount': amount}
        self.undo.new_action(action = 'input_product_made', param = undo_dicta, types = 'func')

        self.func.orders_req_refresh()
        self.output_data()
        return "All clear"



    def delete_product_made(self, product: str, amount: int):
        
        product = product.lower()
        event = self.datafile['event'][0]

        if product in self.datafile['orders_tofill'][event]:
            special_occasion = False
        elif product in self.datafile['orders_tofill'][event]['special_occasion']:
            special_occasion = True
                
        if special_occasion == False:
            if product in self.datafile['product_pending']:
                if amount > self.datafile['product_pending'][product]:
                    amounta = self.datafile['product_pending'][product]
                    return f"There is only {amounta} {product} in reserve, you cannot delete more than {amounta} of {product} from the reserve."
                else: 
                    self.datafile['product_pending'][product] -= amount
                    if self.datafile['product_pending'][product] == 0:
                        del self.datafile['product_pending'][product]
            else:
                return f"There is no {product} to delete."
        elif special_occasion == True:
            if product in self.datafile['product_pending']['special_occasion']:
                if amount > self.datafile['product_pending']['special_occasion'][product]:
                    amounta = self.datafile['product_pending']['special_occasion'][product]
                    return f"There is only {amounta} {product} in reserve, you cannot delete more than {amounta} of {product} from the reserve."
                else:
                    self.datafile['product_pending']['special_occasion'][product] -= amount
                    if self.datafile['product_pending']['special_occasion'][product] == 0:
                        del self.datafile['product_pending']['special_occasion'][product]
            else:
                return f"There is no {product} to delete."

        #undo-redo
        undo_dicta = {'product': product, 'amount': amount}
        self.undo.new_action(action = 'delete_product_made', param = undo_dicta, types = 'func')

        self.func.orders_req_refresh() 
        self.output_data()

        return "All clear"

        
        
    def input_time_spent(self, hour: int, minute: int):

        hours = hour + ( int(minute/60) )
        minutes = minute % 60

        self.datafile['YD_calendar'][self.datetime]['time_spent']['hour'] += hours
        self.datafile['YD_calendar'][self.datetime]['time_spent']['minute'] += minutes
        self.datafile['main_data']['time_spent']['hour'] += hours
        self.datafile['main_data']['time_spent']['minute'] += minutes

        #undo-redo
        undo_dicta = {'hour': hour, 'minute': minute}
        self.undo.new_action(action = 'input_time_spent', param = undo_dicta, types = 'func')

        self.output_data()
        self.func.refresh_YD_timespent(date = self.datetime, hour = hour, minute = minute)
        self.func.refresh_YD_product()
        return "All clear"
        

    def delete_time_spent(self, hour: int, minute: int):

        hours = hour + ( int(minute/60) )
        minutes = minute % 60

        self.datafile['YD_calendar'][self.datetime]['time_spent']['hour'] -= hours
        self.datafile['YD_calendar'][self.datetime]['time_spent']['minute'] -= minutes
        self.datafile['main_data']['time_spent']['hour'] -= hours
        self.datafile['main_data']['time_spent']['minute'] -= minutes

        #undo-redo
        undo_dicta = {'hour': hour, 'minute': minute}
        self.undo.new_action(action = 'delete_time_spent', param = undo_dicta, types = 'func')
        
        self.output_data()
        self.func.refresh_YD_timespent(date = self.datetime, hour = -hour, minute = -minute)
        self.func.refresh_YD_product()
        return f"{hours} hours and {minutes} minutes has been removes from the data."
        

    def input_product_sold(self, amount: int, product: str):
        
        product = product.lower()
        #check special occasion
        if product in self.datafile['type_of_products']:
            special_occasion = False
            product_price = float(self.datafile['type_of_products'][product])
        elif product in self.datafile['type_of_products']['special_occasion']:
            special_occasion = True
            product_price = float(self.datafile['type_of_products']['special_occasion'][product])            
            
        cost = amount * product_price

        if special_occasion == False:

            if product not in self.datafile['product_pending']:
                return f"There is no {product} in the reserve."

            #checking if theres more product sold than in reserve
            if amount >= self.datafile['product_pending'][product]:
                del self.datafile['product_pending'][product]
            else:
                self.datafile['product_pending'][product] -= amount

            #checking if product variable already exists in array
            if product in self.datafile['product_sold']:                    
                self.datafile['product_sold'][product] += amount
            else:
                self.datafile['product_sold'][product] = amount

            #checking if product variable already exists in YD_calendar array
            if product in self.datafile['YD_calendar'][self.datetime]['product_sold']:
                self.datafile['YD_calendar'][self.datetime]['product_sold'][product] += amount
            else:
                self.datafile['YD_calendar'][self.datetime]['product_sold'][product] = amount

            
        elif special_occasion == True:

            if product not in self.datafile['product_pending']:
                return f"There is no {product} in the reserve."

            #checking if theres more product sold than in reserve
            if amount >= self.datafile['product_pending']['special_occasion'][product]:
                del self.datafile['product_pending']['special_occasion'][product]
            else:
                self.datafile['product_pending']['special_occasion'][product] -= amount

            #checking if product variable already exists in array
            if product in self.datafile['product_sold']['special_occasion']:                    
                self.datafile['product_sold']['special_occasion'][product] += amount
            else:
                self.datafile['product_sold']['special_occasion'][product] = amount

            #checking if product variable already exists in YD_calendar array
            if product in self.datafile['YD_calendar'][self.datetime]['product_sold']['special_occasion']:
                self.datafile['YD_calendar'][self.datetime]['product_sold']['special_occasion'][product] += amount
            else:
                self.datafile['YD_calendar'][self.datetime]['product_sold']['special_occasion'][product] = amount
                
        self.datafile['main_data']['revenue'] += cost
        self.datafile['main_data']['profit'] += cost
        self.datafile['YD_calendar'][self.datetime]['revenue'] += cost
        self.datafile['YD_calendar'][self.datetime]['profit'] += cost

        self.func.refresh_YD_revenue(date = self.datetime, revenue = cost)
        self.func.refresh_YD_profit(date = self.datetime, profit = cost)
        self.func.refresh_YD_product()

        self.func.orders_req_refresh()
        self.output_data()
        

    def input_new_product(self, new_product: str, special_occasion: bool, price: float):

        new_product = new_product.lower()
        if new_product in self.datafile['type_of_products'] or new_product in self.datafile['type_of_products']['special_occasion']:
            return f"{new_product.title()} is already in the 'type of product' list."
        
        if special_occasion == False:
            self.datafile['type_of_products'][new_product] = price
        elif special_occasion == True:
            self.datafile['type_of_products']['special_occasion'][new_product] = price

        #undo-redo
        undo_dicta = {'new_product': new_product, 'special_occasion': special_occasion, 'price': price}
        self.undo.new_action(action = 'input_new_product', param = undo_dicta, types = 'func')

        self.output_data()
        return "All clear"


    def change_product_price(self, product: str, price: float):

        product = product.lower()
        preprice = self.datafile['type_of_products'][product]

        if product in self.datafile['type_of_products']:
            self.datafile['type_of_products'][product] = price

        elif product in self.datafile['type_of_products']['special_occasion']:
            self.datafile['type_of_products']['special_occasion'][product] = price
            
        #undo-redo
        undo_dicta = {'product': product, 'price': preprice}
        self.undo.new_action(action = 'change_product_price', param = undo_dicta, types = 'func')
        
        self.output_data()
        

    def delete_new_product(self, del_product: str):

        del_product = del_product.lower()

        price = self.datafile['type_of_products'][del_product]

        if del_product in self.datafile['type_of_products']:
            special_occasion = False
            del self.datafile['type_of_products'][del_product] 
        elif del_product in self.datafile['type_of_products']['special_occasion']:
            special_occasion = True
            del self.datafile['type_of_products']['special_occasion'][del_product]

        self.output_data()
        return "All clear"
    


    def input_new_event(self, event: str, name: str):

        self.datafile['event'].append(event)         
        self.datafile['orders_tofill'][event] = {'special_occasion': {}}
        self.datafile['orders_req_cancellation'][event] = {'special_occasion': {}}
        self.datafile['manual_orders_req_cancellation'][event] = {}
        self.datafile['form_id'][event] = {'input': 0,
                                           'output': 0}
        self.datafile['event_name'][event] = name.title()


        #refresh event order  
        sorted_list = self.datafile['event'].copy()
        sorted_list.sort(key = lambda date: dt.datetime.strptime(date, '%m/%d'))

        copied_otf  = self.datafile['orders_tofill'].copy()
        copied_orc  = self.datafile['orders_req_cancellation'].copy()
        copied_morc = self.datafile['manual_orders_req_cancellation'].copy()
        copied_ena  = self.datafile['event_name'].copy()
        copied_fid  = self.datafile['form_id'].copy()

        self.datafile['event'] = sorted_list
        self.datafile['orders_tofill'] = {}
        self.datafile['orders_req_cancellation'] = {}
        self.datafile['manual_orders_req_cancellation'] = {}
        self.datafile['event_name'] = {}
        self.datafile['form_id'] = {}

        for i in sorted_list:
            self.datafile['orders_tofill'][i] = copied_otf[i]
            self.datafile['orders_req_cancellation'][i] = copied_orc[i]
            self.datafile['manual_orders_req_cancellation'][i] = copied_morc[i]
            self.datafile['event_name'][i] = copied_ena[i]
            self.datafile['form_id'][i] = copied_fid[i]
            

        undo_dicta = {'event': event}
        self.undo.new_action(action = 'input_new_event', param = undo_dicta, types = 'func')

        self.output_data()
        

    def change_event_name(self, name: str):

        event = self.datafile['event'][0]

        prename = self.datafile['event_name'][event]
        self.datafile['event_name'][event] = name.title()

        undo_dicta = {'event': event, 'name': prename}
        self.undo.new_action(action = 'change_event_name', param = undo_dicta, types = 'func')

        self.output_data()
        return "All clear"



    def change_event_date(self, month: int, day: int):

        if month < 0 or day < 0:
            return "Please check your input. Do not enter negative amounts."

        event = self.datafile['event'][0]

        current_year = datetime.today().year
        predate = self.datafile['event'][0]

        month_info = ['January', 'February', 'March',
                      'April', 'May', 'June',
                      'July', 'August', 'September',
                      'October', 'November', 'December'
                      ]

        #check if leap year for february
        if current_year % 400 == 0 or current_year % 100 != 0 and current_year % 4 == 0:
            #if leap year true
            if month == 2:
                if day > 29:
                    return "There is only 29 days in February. Please check your input."

        else:
            #if leap year false
            if month == 2:
                if day > 28:
                    return "There is only 28 days in February. Please check your input."

        short_month = [4, 6, 9, 11]
        long_month = [1, 3, 5, 7, 8, 10, 12]

        month_name = month_info[month - 1]

        if month in short_month:
            #if more than 30 days in specific months
            if day > 30:
                return f"There is only 30 days in {month_name}. Please check your input."

        elif month in long_month:
            #if more than 31 days in specific months
            if day > 31:
                return f"There is only 31 days in {month_name}. Please check your input."

        #construct date
        date = f"{str(month)}/"
        if len(str(day)) == 1:
            date += '0'
            date += str(day)
        elif len(str(day)) == 2:
            date += str(day)
            
        self.datafile['orders_to_fill'][date] = self.datafile['orders_to_fill'].pop(predate)
        self.datafile['orders_req_cancellation'][date] = self.datafile['orders_req_cancellation'].pop(predate)
        self.datafile['manual_orders_req_cancellation'][date] = self.datafile['manual_orders_req_cancellation'].pop(predate)

        #changing date in self.datafile['event'] and ['event_name']
        predict_event = self.datafile['event'].copy()
        predict_name = self.datafile['event_name'].copy()
        prename = self.datafile['event_name'][predate]

        event_index = predict_event.index(predate)
        name_index = predict_name.index(prename)

        self.datafile['event'] = []
        self.datafile['event'].append(date)
        for i in range(len(predict_event) - 1):
            self.datafile['event'].append(predict_event[i + 1])

        self.datafile['event_name'] = {}
        self.datafile['event_name'][date] = predict_name[prename]
        for i in range(len(predict_name) - 1):
            initial_date = list(predict_name)[i + 1]
            initial_name = predict_name[initial_date]
            self.datafile['event_name'][initial_date] = initial_name

        undo_dicta = {'month': month, 'day': day}
        self.undo.new_action(action = 'change_event_date', param = undo_dicta, types = 'func')
            
        self.output_data()

        return "All clear"



    def delete_event(self, event: str):

        self.datafile['event'].remove(event)

        del self.datafile['orders_tofill'][event]
        del self.datafile['orders_req_cancellation'][event]
        del self.datafile['manual_orders_req_cancellation'][event]
        del self.datafile['form_id'][event]
        del self.datafile['event_name'][event]

        self.output_data()
        
        return "All clear"



    def input_event_product(self, product: str):

        if self.datafile['event'] != []:
        
            #this is to add products from original-larger list to specific events
            event = self.datafile['event'][0]
            product = product.lower()
            
            if product in self.datafile['type_of_products']:
                self.datafile['orders_tofill'][event][product] = 0
                self.datafile['product_pending'][product] = 0
            elif product in self.datafile['type_of_products']['special_occasion']:
                self.datafile['orders_tofill'][event]['special_occasion'][product] = 0
                self.datafile['product_pending']['special_occasion'][product] = 0
                
            undo_dicta = {'product': product}
            self.undo.new_action(action = 'input_event_product', param = undo_dicta, types = 'func')

            self.output_data()

            return "All clear"


    def delete_event_product(self, product: str):
        
        #this is to remove products from specific events
        event = self.datafile['event'][0]
        product = product.lower()
        
        if product in self.datafile['type_of_products']:

                del self.datafile['orders_tofill'][event][product] 
                return f"{product.title()} has been successfully removed from the list for {event_name}."
            
        elif product in self.datafile['type_of_products']['special_occasion']:

                del self.datafile['orders_tofill'][event]['special_occasion'][product] 
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


    def refresh_YD_revenue(self, date: str, revenue: int):
        
        lista = []
        for i in self.datafile['YD_calendar']:
            lista.append(i)

        index = lista.index(date) + 1

        for i in range(len(lista) - index):
            #variable is the refined index that this loop uses
            variable = list(self.datafile['YD_calendar'])[i + index]
            self.datafile['YD_calendar'][variable]['revenue'] += revenue
        
        self.output_data()
    

    def refresh_YD_cost(self, date: str, cost: int):

        lista = []
        for i in self.datafile['YD_calendar']:
            lista.append(i)

        index = lista.index(date) + 1

        for i in range(len(lista) - index):
            #variable is the refined index that this loop uses
            variable = list(self.datafile['YD_calendar'])[i + index]
            self.datafile['YD_calendar'][variable]['cost'] += cost

        self.output_data()


    def refresh_YD_profit(self, date: str, profit: int):

        lista = []
        for i in self.datafile['YD_calendar']:
            lista.append(i)

        index = lista.index(date) + 1

        for i in range(len(lista) - index):
            #variable is the refined index that this loop uses
            variable = list(self.datafile['YD_calendar'])[i + index]
            self.datafile['YD_calendar'][variable]['profit'] += profit

        self.output_data()


    def refresh_YD_timespent(self, date: str, hour: int, minute: int):

        lista = []
        for i in self.datafile['YD_calendar']:
            lista.append(i)

        index = lista.index(date) + 1

        for i in range(len(lista) - index):
            #variable is the refined index that this loop uses
            variable = list(self.datafile['YD_calendar'])[i + index]

            initial_hour = self.datafile['YD_calendar'][variable]['time_spent']['hour']
            initial_minute = self.datafile['YD_calendar'][variable]['time_spent']['minute']
            self.datafile['YD_calendar'][variable]['time_spent']['hour'] = initial_hour + hour + ( int( (minute + initial_minute) /60) )
            if minute + initial_minute < 0:
                self.datafile['YD_calendar'][variable]['time_spent']['hour'] -= 1
            self.datafile['YD_calendar'][variable]['time_spent']['minute'] = (minute + initial_minute) % 60

        self.output_data()


    def refresh_YD_product(self):

        time_spent_YD = {'hour': 0, 'minute': 0}
        hours = 0
        minutes = 0
        
        self.datafile['product_sold_YD'] = { 'special_occasion': {} }
        self.datafile['net_loss_YD'] = { 'special_occasion': {} }

        #refreshes main data in YD_calendar, filling the 0s with previous data.
        for i in self.datafile['YD_calendar']:
            
            index = list(self.datafile['YD_calendar']).index(i)
            prev = list(self.datafile['YD_calendar'])[index - 1]

            if self.datafile['YD_calendar'][i]['revenue'] == 0:
                self.datafile['YD_calendar'][i]['revenue'] = self.datafile['YD_calendar'][prev]['revenue']

            if self.datafile['YD_calendar'][i]['cost'] == 0:
                self.datafile['YD_calendar'][i]['cost'] = self.datafile['YD_calendar'][prev]['cost']

            if self.datafile['YD_calendar'][i]['time_spent']['hour'] == 0:
                self.datafile['YD_calendar'][i]['time_spent']['hour'] = self.datafile['YD_calendar'][prev]['time_spent']['hour']

            if self.datafile['YD_calendar'][i]['time_spent']['minute'] == 0:
                self.datafile['YD_calendar'][i]['time_spent']['minute'] = self.datafile['YD_calendar'][prev]['time_spent']['minute']
                
                
        for i in self.datafile['YD_calendar']:

            self.datafile['YD_calendar'][i]['profit'] = self.datafile['YD_calendar'][i]['revenue'] - self.datafile['YD_calendar'][i]['cost']

            hours += self.datafile['YD_calendar'][i]['time_spent']['hour']
            minutes += self.datafile['YD_calendar'][i]['time_spent']['minute']

            for j in self.datafile['YD_calendar'][i]['product_sold']:
                if j != 'special_occasion':
                    if j not in self.datafile['product_sold_YD']:
                        self.datafile['product_sold_YD'][j] = self.datafile['YD_calendar'][i]['product_sold'][j]
                    elif j in self.datafile['product_sold_YD']:
                        self.datafile['product_sold_YD'][j] += self.datafile['YD_calendar'][i]['product_sold'][j]

                elif j == 'special_occasion':
                    for k in self.datafile['YD_calendar'][i]['product_sold']['special_occasion']:
                        if k not in self.datafile['product_sold_YD']['special_occasion']:
                            self.datafile['product_sold_YD']['special_occasion'][k] = self.datafile['YD_calendar'][i]['product_sold']['special_occasion'][k]
                        elif k in self.datafile['product_sold_YD']['special_occasion']:
                            self.datafile['product_sold_YD']['special_occasion'][k] += self.datafile['YD_calendar'][i]['product_sold']['special_occasion'][k]

            for j in self.datafile['YD_calendar'][i]['net_loss']:
                if j != 'special_occasion':
                    if j not in self.datafile['net_loss_YD']:
                        self.datafile['net_loss_YD'][j] = self.datafile['YD_calendar'][i]['net_loss'][j]
                    elif j in self.datafile['net_loss_YD']:
                        self.datafile['net_loss_YD'][j] += self.datafile['YD_calendar'][i]['net_loss'][j]

                elif j == 'special_occasion':
                    for k in self.datafile['YD_calendar'][i]['net_loss']['special_occasion']:
                        if k not in self.datafile['net_loss_YD']['special_occasion']:
                            self.datafile['net_loss_YD']['special_occasion'][k] = self.datafile['YD_calendar'][i]['net_loss']['special_occaison'][k]
                        elif k in self.datafile['net_loss_YD']['special_occasion']:
                            self.datafile['net_loss_YD']['special_occasion'][k] += self.datafile['YD_calendar'][i]['net_loss']['special_occasion'][k]


        self.datafile['main_data']['time_spent_YD'] = self.datafile['YD_calendar'][list(self.datafile['YD_calendar'])[-1]]['time_spent']
        self.datafile['main_data']['revenue_YD'] = self.datafile['YD_calendar'][list(self.datafile['YD_calendar'])[-1]]['revenue']
        self.datafile['main_data']['cost_YD'] = self.datafile['YD_calendar'][list(self.datafile['YD_calendar'])[-1]]['cost']
        self.datafile['main_data']['profit_YD'] = self.datafile['YD_calendar'][list(self.datafile['YD_calendar'])[-1]]['profit']

        self.output_data()


    def check_YD_calendar(self):
        #to add 365 days in the calendar
        #self.datafile['YD_calendar'][self.datetime] = {'revenue': 0, 'cost': 0, 'profit': 0, 'time_spent': 0, 'product_sold': {}}

        dicta = {'revenue': 0,
                 'cost': 0,
                 'profit': 0,
                 'time_spent': {'hour': 0, 'minute': 0},
                 'product_sold': {'special_occasion': {}},
                 'net_loss': {'special_occasion': {}}
                 }

        if bool(self.datafile['YD_calendar']) ==  False:
            start = datetime(int(self.year), 1, 1, 0, 0, 0)
            end = datetime(int(self.year), 12, 31, 0, 0, 0)
            delta = end - start
            for i in range(delta.days + 1):
                self.datafile['YD_calendar'][(start + timedelta(days = i)).strftime('%Y/%m/%d')] = dicta
        else:
            year_of_datafile = list(self.datafile['YD_calendar'])[0][:4]
            start = datetime(int(self.year), 1, 1, 0, 0, 0)
            end = datetime(int(self.year), 12, 31, 0, 0, 0)
            delta = end - start
            if year_of_datafile != self.year: #if the year of datafile is predated then empty the dictionary and create a new one for the new year.
                self.datafile['YD_calendar'] = {}
                for i in range(delta.days + 1):            
                    self.datafile['YD_calendar'][(start + timedelta(days=i)).strftime('%Y/%m/%d')] = dicta
                    
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

        if self.datafile['event'] != []:

            event = self.datafile['event'][0]
            self.orders_req_refresh()

            for i in self.datafile['orders_tofill'][event]:
                if i != 'special_occasion':
                    dict_pending[i] = 0
                else:
                    dict_pending['special_occasion'] = {}
                    for k in self.datafile['orders_tofill'][event]['special_occasion']:
                        dict_pending['special_occasion'][k] = 0

            for i in self.datafile['orders_req_cancellation'][event]:
                if i != 'special_occasion':
                    dict_pending[i] += self.datafile['orders_req_cancellation'][event][i]
                else:
                    for k in self.datafile['orders_req_cancellation'][event]['special_occasion']:
                        dict_pending['special_occasion'][k] += self.datafile['orders_req_cancellation'][event]['special_occasion'][k]

            for i in self.datafile['product_pending']:
                if i != 'special_occasion':
                    dict_pending[i] -= self.datafile['product_pending'][i]
                else:
                    for k in self.datafile['product_pending']['special_occasion']:
                        dict_pending['special_occasion'][k] += self.datafile['product_pending']['special_occasion'][k]
            
            self.datafile['orders_tofill'][event] = dict_pending
            
        self.output_data()
        

    def orders_req_refresh(self):

        dicta = {'special_occasion': {}}

        for i in range(len(self.datafile['manual_orders_req_cancellation'])):
            event = list(self.datafile['manual_orders_req_cancellation'])[i] 
            lena = list(self.datafile['manual_orders_req_cancellation'][event]) #how many people ordered
            for j in lena: #j = name of people ordered
                for k in self.datafile['manual_orders_req_cancellation'][event][j]: #k = name of people ordered
                    #name of product = k
                    if k != 'special_occasion':
                        if k not in dicta:
                            dicta[k] = 0
                        dicta[k] += self.datafile['manual_orders_req_cancellation'][event][j][k]
                    elif k == 'special_occasion':
                        for l in self.datafile['manual_orders_req_cancellation'][event][j]['special_occasion']:
                            #name of special product = l
                            if l not in dicta['special_occasion']:
                                dicta['special_occasion'][l] = 0
                            dicta['special_occasion'][l] += self.datafile['manual_orders_req_cancellation'][event][j]['special_occasion'][l]

            self.datafile['orders_req_cancellation'][event] = dicta
            
        self.output_data()
        

    def check_all(self):

        self.check_YD_calendar()
        self.refresh_YD_product()
        self.check_event_remove()




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
    
    path = 'undo.json'

    new_main_dict = {}
    dump_obj = json.dumps(new_main_dict, indent = 4)
    with open("undo.json", "w") as datafile:
        datafile.write(dump_obj)
    with open("undo.json", "r") as datafile:
        data = json.load(datafile)
            
    return data
    

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
        




    

    
