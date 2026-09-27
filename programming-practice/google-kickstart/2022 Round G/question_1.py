
num = int(input())

for i in range(num):
    numba = i + 1
    john = list(map(int, input().split()))
    count = 0
    max_each_day = []
    data = []
    for i in range(john[0]):
        #temp = list(map(int, input().split()))
        data.append(list(map(int, input().split())))
    for i in range(john[1]):
        temp_days = []
        for j in range(john[0]):
            temp_days.append(data[j][i])
        max_each_day.append(max(temp_days))
    for i in range(john[1]):
        if data[john[2]-1][i] < max_each_day[i]:
            count += (max_each_day[i] - data[john[2]-1][i])
    
    
    print(f"Case #{numba}: {count}")
        
    
