p1name=input("Player 1 please enter your name: ")
p2name=input("Player 2 please enter your name: ")
p1sign=input("Player 1 enter your sign: ")
p2sign=input("Player 2 enter your sign: ")

matrix_size=int(input("Please enter matrix size: "))

no_of_input = matrix_size*matrix_size

def print_matrix():
    tempGridNumber = 1
    for i in range(matrix_size):
        for j in range(matrix_size):
            if(matrix[i][j] == 0):
                print(tempGridNumber,"  ",end=" ")
            else:
                print(matrix[i][j],"  ",end=" ")
            tempGridNumber+=1
        print("")

matrix= [[0 for x in range(matrix_size)] for y in range(matrix_size)]

print_matrix()

Player1=[]
Player2=[]

for input_time in range(0,no_of_input):
    if(input_time % 2)!=0:
        p1position=int(input("Player 1 enter position: ")) 
        Player1.append(p1position)
        i = int ((p1position-1) / matrix_size)
        j = int ((p1position-1) % matrix_size)
        matrix[i][j] = p1sign
        print_matrix()
    else:
        p2position=int(input("Player 2 enter position: ")) 
        Player2.append(p2position)
        i = int ((p2position-1) / matrix_size)
        j = int ((p2position-1) % matrix_size)
        matrix[i][j] = p2sign
        print_matrix()
print(Player1)
print(Player2)
print("grid is full")

winnig=[]

horizontalTemp = []
horizontalStart = 1

verticalTemp = []

forwordCrossTemp = []
forwordstart=1

backwordCrossTemp = []
backwordstart = matrix_size
backtemp=matrix_size

for i in range(1,matrix_size+1):
    verticalStart = i
    for j in range(1,matrix_size+1):
        horizontalTemp.append(horizontalStart)
        horizontalStart += 1

        verticalTemp.append(verticalStart)
        verticalStart+=matrix_size

        if (i == j):
            forwordCrossTemp.append(forwordstart)
        forwordstart+=1

        if (backtemp == j):
            backwordCrossTemp.append(backwordstart)
    backwordstart+=(matrix_size-1)

    winnig.append(horizontalTemp)
    winnig.append(verticalTemp)
    verticalTemp = []
    horizontalTemp = []
backtemp-=1
winnig.append(forwordCrossTemp)
winnig.append(backwordCrossTemp)

print(winnig)