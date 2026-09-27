import matplotlib.pyplot as plt
import json
import datetime as dt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


window = tk.Tk()
window.geometry("1280x785")
window.configure(bg = "#000000")

with open("data test for chart.json", "r") as datafile:
    data = json.load(datafile)

def create_chart(chart_type: str, year_over: str , data: dict, x_cord: int, y_cord: int):

    datea = []
    revenuea = []
    costa = []
    profita = []
    timespenta = []

    #current_date = dt.datetime.now().strftime('%Y/%m/%d')
    current_date = '2022/04/04'
    index_checker = 0

    for i in range(len(data['YD_calendar'])):

        datee = list(data['YD_calendar'])[i]

        if datee == current_date:
            index_checker = i

        
    for i in data['YD_calendar']:
        
        current_index = list(data['YD_calendar']).index(i)
        datea.append(dt.datetime.strptime(i, '%Y/%m/%d'))

        revenue_num = data['YD_calendar'][i]['revenue']

        if current_index <= index_checker:
            revenue_num = data['YD_calendar'][i]['revenue']
            cost_num = data['YD_calendar'][i]['cost']
            profit_num = data['YD_calendar'][i]['profit']

            timespent_min = data['YD_calendar'][i]['time_spent']['minute']
            timespent_hour = data['YD_calendar'][i]['time_spent']['hour']
            timespent_comp = timespent_hour + (timespent_min / 60)
            
            revenuea.append(revenue_num)
            costa.append(cost_num)
            profita.append(profit_num)
            timespenta.append(timespent_comp)
            
        else:
            
            revenuea.append(None)
            costa.append(None)
            profita.append(None)
            timespenta.append(None)
            

    if year_over == 'over':

        revenueo = data['main_data']['revenue']
        costo = data['main_data']['cost']
        profito = data['main_data']['profit']

        timespento_min = data['main_data']['time_spent']['minute']
        timespento_hour = data['main_data']['time_spent']['hour']
        timespento = timespento_hour + (timespento_min / 60)
        
        tester = []
        final_value = 0

        for i in range(len(revenuea)):
            if revenuea[i] != None:
                tester.append(revenuea[i])

        final_value = len(tester) - 1

        revenue_diff = revenueo - revenuea[final_value]
        cost_diff = costo - costa[final_value]
        profit_diff = profito - profita[final_value]
        timespent_diff = timespento - timespenta[final_value]

        for i in range(len(revenuea)):
            
            if revenuea[i] != None:
                revenuea[i] = revenuea[i] + revenue_diff
                costa[i] = costa[i] + cost_diff
                profita[i] = profita[i] + profit_diff
                timespenta[i] = timespenta[i] + timespent_diff
                
    plt.rcParams.update({'font.size': 2})
    
    if chart_type == 'revenue':

        fig, ax1 = plt.subplots()
        fig.set_size_inches(2, 1.5)
        ax1.plot(datea, revenuea, color = 'white', linewidth=1)
        fig.autofmt_xdate()

    elif chart_type == 'cost':

        fig, ax1 = plt.subplots()
        fig.set_size_inches(2, 1.5)
        ax1.plot(datea, costa, color = 'white', linewidth=1)
        fig.autofmt_xdate()

    elif chart_type == 'profit':

        fig, ax1 = plt.subplots()
        fig.set_size_inches(1.8, 1)
        ax1.plot(datea, profita, color = 'white', linewidth=1)
        fig.autofmt_xdate()

    elif chart_type == 'timespent':

        fig, ax1 = plt.subplots()
        fig.set_size_inches(2, 1.5)
        ax1.plot(datea, timespenta, color = 'white', linewidth=1)
        fig.autofmt_xdate()
    
    fig.patch.set_facecolor('#0E1012')
    ax1.patch.set_facecolor('#0E1012')

    ax1.spines.right.set_visible(False)
    ax1.spines.top.set_visible(False)
    ax1.xaxis.set_visible(False)
    ax1.yaxis.set_visible(False)
    
    ax1.spines['bottom'].set_color('white')
    ax1.spines['left'].set_color('white')
    
    canvas = FigureCanvasTkAgg(fig, master = window)
    canvas.draw()

    if chart_type == 'revenue':

        global chart_revenue
        try:
            chart_revenue
        except NameError:
            pass
        else:
            chart_revenue.destroy()
        
        chart_revenue = canvas.get_tk_widget()
        chart_revenue.place(x=x_cord, y=y_cord)

    elif chart_type == 'cost':

        global chart_cost
        try:
            chart_cost
        except NameError:
            pass
        else:
            chart_cost.destroy()
        
        chart_cost = canvas.get_tk_widget()
        chart_cost.place(x=x_cord, y=y_cord)

    elif chart_type == 'profit':

        global chart_profit
        try:
            chart_profit
        except NameError:
            pass
        else:
            chart_profit.destroy()
        
        chart_profit = canvas.get_tk_widget()
        chart_profit.place(x=x_cord, y=y_cord)

    elif chart_type == 'timespent':

        global chart_timespent
        try:
            chart_timespent
        except NameError:
            pass
        else:
            chart_timespent.destroy()
        
        chart_timespent = canvas.get_tk_widget()
        chart_timespent.place(x=x_cord, y=y_cord)
        

    

    
create_chart(chart_type = 'profit', year_over = 'over', data = data, x_cord = 555, y_cord = 382)

