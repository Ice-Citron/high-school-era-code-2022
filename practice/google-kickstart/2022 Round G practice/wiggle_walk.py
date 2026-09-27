
def process(case_num, info, direction):
    
    #create empty 2D array of boolean based on row and col

    #the number of instructions,
    #the number of rows,
    #the number of columns,
    #the robot's starting row,
    #the robot's starting column, 
    
    empty = []
    for i in range(info[1]):
        empty.append([False for i in range(info[2])])

    #empty [y cord - 1] [x cord - 1]

    #starting x and y cord
    x_cord = info[4] - 1
    y_cord = info[3] - 1
    empty[y_cord][x_cord] = True

    for i in direction:
        if i == 'N':
            #check if already occupied
            temp_y_cord = y_cord - 1
            while True:
                if empty[temp_y_cord][x_cord] == False:
                    empty[temp_y_cord][x_cord] = True
                    y_cord -= 1
                    break
                temp_y_cord -= 1
                y_cord -= 1
            
        elif i == 'E':
            #check if already occupied
            temp_x_cord = x_cord + 1
            while True:
                if empty[y_cord][temp_x_cord] == False:
                    empty[y_cord][temp_x_cord] = True
                    x_cord += 1
                    break
                temp_x_cord += 1
                x_cord += 1
        
        elif i == 'S':
            #check if already occupied
            temp_y_cord = y_cord + 1
            while True: 
                if empty[temp_y_cord][x_cord] == False:
                    empty[temp_y_cord][x_cord] = True
                    check = True
                    y_cord += 1
                    break
                temp_y_cord += 1
                y_cord += 1
        
        elif i == 'W':
            #check if already occupied
            temp_x_cord = x_cord - 1
            while True:
                if empty[y_cord][temp_x_cord] == False:
                    empty[y_cord][temp_x_cord] = True
                    check = True
                    x_cord -= 1
                    break
                temp_x_cord -= 1
                x_cord -= 1
       
    print(f"Case #{case_num + 1}: {y_cord+1} {x_cord+1}")


for i in range(int(input())):
    array = list(map(int, input().split()))
    direction = [x for x in str(input())]
    process(i, array, direction)

    
