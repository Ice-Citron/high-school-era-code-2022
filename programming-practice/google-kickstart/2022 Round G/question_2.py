
num = int(input())


for i in range(num):
    casea = i+1
    count_l = 0
    count_r = 0
    radius_small, radius_house = map(int, input().split())
    list_l = []
    list_r = []
    
    for i in range(int(input())):
        temp_cord = tuple(map(int, input().split()))
        list_l.append(temp_cord)
    
    for i in range(int(input())):
        temp_cord = tuple(map(int, input().split()))
        list_r.append(temp_cord)

    bool_list_l = []
    bool_list_r = []

    for i in range(len(list_l)):
        x_cord = list_l[i][0]
        y_cord = list_l[i][1]
        value = (x_cord**2 + y_cord**2)**0.5
        if radius_house > (value - radius_small):
            bool_list_l.append(value - radius_small)
        elif radius_house == (value - radius_small):
            bool_list_l.append(value - radius_small)

    for i in range(len(list_r)):
        x_cord = list_r[i][0]
        y_cord = list_r[i][1]
        value = (x_cord**2 + y_cord**2)**0.5
        if radius_house > (value - radius_small):
            bool_list_r.append(value - radius_small)
        elif radius_house == (value - radius_small):
            bool_list_r.append(value - radius_small)


    if len(bool_list_l) != 0 and len(bool_list_r) != 0:
        
        min_l = min(bool_list_l)
        min_r = min(bool_list_r)
        
        for i in range(len(bool_list_r)):
            if bool_list_r[i] > min_l:
                bool_list_r[i] = None
        for i in range(len(bool_list_l)):
            if bool_list_l[i] > min_r:
                bool_list_l[i] = None

        bool_list_l = [i for i in bool_list_l if i != None]
        bool_list_r = [i for i in bool_list_r if i != None]


            
    print(f"Case #{casea}: {len(bool_list_l)} {len(bool_list_r)}")












    
