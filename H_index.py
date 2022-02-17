#author Subrahmanyam Pampana
#problem statement https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000941e56
def processCase(test_case):
    num_papers = int(input())
    num_citations = list(map(int,input().split()))
    res = []
    maxhidx = 0
    for i in range(num_papers):
        k = maxhidx+1
        while k<=i+2:
            count=0
            for j in range(i+1):
                    if num_citations[j]>=k:
                        count+=1
            if count!=k:
              res.append(k-1)
              maxhidx = max(maxhidx,k-1)
              break;
            k+=1

    res = ' '.join(map(str,res))        
    print(f"Case #{test_case}: {res}") 
    
test_cases = int(input()) 
for i in range(test_cases):
    processCase(i+1)
            
            

