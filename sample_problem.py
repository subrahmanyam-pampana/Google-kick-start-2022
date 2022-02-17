# author: subrahmanyam Pampana
# problem statement https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000942404
def destributeCandies(test_case):
    #read inputs
    (num_candy_bags,num_kids)= tuple(map(int,input().split()))
    candy_array = list(map(int,input().split()))
    total_candies = 0
    for x in candy_array:
        total_candies+=x
    rem =  total_candies%num_kids  
    print(f"Case #{test_case}: {rem}")
test_cases = int(input())
for i in range(test_cases):
    destributeCandies(i+1)
