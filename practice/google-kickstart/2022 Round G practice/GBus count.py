
def number_between(value, first, last):
    if first <= value <= last:
        return 1
    else:
        return 0


def process_case(case_num, bus_num, routes, target):
    lista = []
    for i in target:
        lista.append(0)
        for j in range(bus_num):
            lista[target.index(i)] += number_between(i, routes[j][0], routes[j][1])
    return_text = f"Case #{case_num}:"
    for i in lista:
        return_text = return_text + " " + str(i)
    print(return_text)


for i in range(int(input())):
    
    bus_num = input()
    if bus_num == '':
        bus_num = int(input())
    else:
        bus_num = int(bus_num)
    data = list(map(int, input().split()))
    target = []
    bus_cords = [tuple(data[i:i+2]) for i in range(0, len(data),2)]
    target_num = int(input())
    for i in range(target_num): target.append(int(input()))
    process_case(i, bus_num, bus_cords, target)
        








