
lista = [1, 1, 0, 3, 0, 0, 0, 4, 0, 0, 5, 5, 0, 0, 0, 0]
listb = []

dicta = {'1': 0, '2': 0, '3': 0, '4': 3, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

def refresh():
    for i in range(len(lista)):
        
        if lista[i] == 0:
            lista.insert(i, lista[i - 1])
            lista.remove(0)

    for i in dicta:
        
        index = list(dicta).index(i)
        if index == 0:
            prev = list(dicta)[index]
        else:
            prev = list(dicta)[index - 1]
        
        if dicta[i] == 0:
            dicta[i] = dicta[prev]
            

refresh()
print(dicta)

def add(cords: str, amount: int):

    lista = []

    for i in dicta:
        lista.append(i)

    index = lista.index(cords)

    for i in range(len(dicta) - index):
        variable = list(dicta)[i + index]
        dicta[variable] += amount




add(cords = '3', amount = 5)

print(dicta)



















    def refresh_YD_revenue(self, date: str, revenue: int):
            
        lista = []
        for i in self.datafile['YD_calendar']:
            lista.append(i)

        index = lista.index(date)

        for i in range(len(lista) - index):
            #variable is the refined index that this loop uses
            variable = list(self.datafile['YD_calendar'])[i + index]
            self.datafile['YD_calendar'][variable]['revenue'] += revenue
        
        self.output_data(len)
        pass
    

    def refresh_YD_cost(self, date: str, cost: int):

        lista = []
        for i in self.datafile['YD_calendar']:
            lista.append(i)

        index = lista.index(date)

        for i in range(len(lista) - index):
            #variable is the refined index that this loop uses
            variable = list(self.datafile['YD_calendar'])[i + index]
            self.datafile['YD_calendar'][variable]['cost'] += cost

        self.output_data()
        pass


    def refresh_YD_profit(self, date: str, profit: int):

        lista = []
        for i in self.datafile['YD_calendar']:
            lista.append(i)

        index = lista.index(date)

        for i in range(len(lista) - index):
            #variable is the refined index that this loop uses
            variable = list(self.datafile['YD_calendar'])[i + index]
            self.datafile['YD_calendar'][variable]['profit'] += profit

        self.output_data()
        pass

    
    def refresh_YD_timespent(self, date: str, hour: int, minute: int):
        

    def refresh_YD_product(self):






    
