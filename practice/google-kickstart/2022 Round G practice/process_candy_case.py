def process_case(case_num):
    
    (num_candy_bag, num_kids) = tuple(map(int, input().split()))
    candy_count = list(map(int, input().split()))
    
    total_candy = 0
    for i in range(num_candy_bag):
        total_candy += candy_count[i]
    
    amount_remaining = total_candy % num_kids
    
    print(f"Case #{case_num}: {amount_remaining}")

case_amount = int(input())
for i in range(case_amount):
    process_case(i+1)
