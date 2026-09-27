"""
3
1 1 5 3
1 2 4 5
1 1 2 2
A B N K

"""


def process_case(case_num, info):
    #random number picked, positive i and j
    #i and j is <= N
    #they are eating i^A and j^B amount of sprouts
    

    #process out what i and j could be? - ideas
    #based on A and B, ie power values, list out the their outputs to the <N^A or <N^B
    NA_list = []
    NB_list = []

    for i in range(1, info[2]+1): #info[2] is N
        NA_list.append(i**info[0]) #info[0] is A
        NB_list.append(i**info[1]) #info[1] is B
    
    #add all possible values against each other and check if divisible by K? #lots of for loops
    total_val = 0

    for i in range(len(NA_list)):
        for j in range(len(NB_list)):
            if i != j:
                temp_sum = NA_list[i] + NB_list[j]
                print(str(NA_list[i]) + " " + str(NB_list[j]))
                if temp_sum % info[3] == 0: #info[3] is K
                    total_val += 1
    
    #return output is num of pairs when watson+sherlock gets along
    #return modulo if number is high 10**9 eg.

    print(f"Case #{case_num + 1}: {total_val}")


cases = int(input())

for i in range(cases):
    info = list(map(int, input().split()))
    process_case(i, info)
