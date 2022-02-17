#author: subrahmanyam Pampana
# problem statement https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000941ec5
def processTestCase(test_case):
    #read the kingdom name and convert it
    kingdom_name = str(input())
    last_letter = kingdom_name[-1]
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    
    if last_letter in vowels:
        print(f"Case #{test_case}: {kingdom_name} is ruled by Alice.")
    elif last_letter.lower() != 'y':
        print(f"Case #{test_case}: {kingdom_name} is ruled by Bob.")
    else:
        print(f"Case #{test_case}: {kingdom_name} is ruled by nobody.")
num_test_cases = int(input())
for i in range(num_test_cases):
    processTestCase(i+1)
