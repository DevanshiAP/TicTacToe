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

for input_time in range(0,no_of_input):
    if(input_time % 2)!=0:
        p1position=int(input("Player 1 enter position: ")) - 1
        i = int (p1position / matrix_size)
        j = int (p1position % matrix_size)
        matrix[i][j] = p1sign
        print_matrix()
    else:
        p2position=int(input("Player 2 enter position: ")) - 1
        i = int (p2position / matrix_size)
        j = int (p2position % matrix_size)
        matrix[i][j] = p2sign
        print_matrix()

print("grid is full")