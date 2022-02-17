#author: Subrahmanyam Pampana
#problem statement https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000942527
#this solution giving wrong answer in the test sets. this is only passing sample test cases
def processTestCase(test_case):
    #read input
    dim = int(input())
    board =[]
    for i in range(dim):
        board.append(list(input()))
    #check rules are matched or not
    num_B,num_R = 0,0
    for i in range(dim):
      for j in range(dim):
        if board[i][j]=='B':
          num_B+=1
        if board[i][j]=='R':
          num_R+=1  
    dif = abs(num_B-num_R)
    if dif>1:
        print(f"Case #{test_case}: Impossible")
        return
    #check B and R winning chanses
    Rcount = 0
    Bcount = 0
    visited = {}
    def findRpaths(i,j):
      nonlocal Rcount
      if j<0:
        return 
      if j>dim-1 or i>dim-1 or i<0 or j<0:
        return
      if i==dim-1 and board[i][j] == 'R':
        Rcount+=1
        return  
      # print(i,j,board[i][j])
      if  board[i][j] == 'R' and (i,j) not in visited:  
          visited[(i,j)] = True
          findRpaths(i,j+1)  #move right
          findRpaths(i,j-1)  #move left 
          findRpaths(i+1,j)  #move down
      else: return    
      return False   

    def findBpaths(i,j):
      nonlocal Bcount
      if j>dim-1 or i>dim-1 or i<0 or j<0:
        return
      if j==dim-1 and board[i][j] == 'B':
        Bcount+=1
        return
      if board[i][j] == 'B' and (i,j) not in visited:  
          visited[(i,j)] = True
          findBpaths(i,j+1)  #move forward 
          findBpaths(i+1,j)  #move down
          findBpaths(i-1,j)  #move up
      return False   
    #Check number of R paths from top to bottom
    for idx,x in enumerate(board[0]):
      if x == 'R':
        findRpaths(0,idx)
    visited = {}
    #check number of B paths from Left to right
    for i in range(dim):
      if board[i][0] == 'B':
        findBpaths(i,0)

    if Bcount>1 or Rcount>1:
      print(f"Case #{test_case}: Impossible")
    elif Bcount==1:
      print(f"Case #{test_case}: Blue wins")
    elif Rcount==1:
      print(f"Case #{test_case}: Red wins")
    else:
      print(f"Case #{test_case}: Nobody wins")


test_cases = int(input())
for i in range(test_cases):
    processTestCase(i+1)
            
            

