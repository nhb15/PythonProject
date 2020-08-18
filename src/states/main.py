print("Hello! \nWelcome to our tic-tac-toe game. ")

name1 = input("Please enter the name of player 1: ")
name2 = input("Please enter the name of player 2: ")

# rand_num = randint(0,9)

print(name1 + " will be X's")
print(name2 + " will be O's")

end = False

while end == False:

    matrix = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    print("_________________________ \n \n")
    print(matrix[0] + "|" + matrix[1] + "|" + matrix[2])
    # print()
    # print()
    print("________")
    print(matrix[3] + "|" + matrix[4] + "|" + matrix[5])
    print("________")
    print(matrix[6] + "|" + matrix[7] + "|" + matrix[8])
    # if matrix matches any of the winnable combinations OR we fill the board, set end to True
    end = True

# POSSIBLE COMBINATIONS

# vertical
# (0,3,6)
# (1,4,7)
# (2,5,8)

# horizontal
# (0,1,2)
# (3,4,5)
# (6,7,8)

# diagonal
# (0,4,8)
# (2,4,6)
