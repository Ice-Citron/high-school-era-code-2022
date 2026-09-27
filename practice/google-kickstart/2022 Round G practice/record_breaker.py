def process_variable(value):
    
    iteration = int(input())
    lista = list(map(int, input().split()))
    true_value, largest_value = 0, 0
    
    for i in range(iteration):
        #if i is first number
        if i == 0:
            if lista[i+1] < lista[i]:
                if lista[i] > largest_value:
                    largest_value = lista[i]
                    true_value += 1
        #if i is last number
        elif i+1 == iteration:
            if lista[i-1] < lista[i]:
                if lista[i] > largest_value:
                    largest_value = lista[i]
                    true_value += 1

        else:
            if lista[i+1] < lista[i] and lista[i-1] < lista[i]:
                if lista[i] > largest_value:
                    largest_value = lista[i]
                    true_value += 1

    print(f"Case #{value}: {true_value}")

num_case = int(input())

for i in range(num_case):
    process_variable(i+1)


