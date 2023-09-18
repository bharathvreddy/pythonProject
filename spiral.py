def generateMatrix(A):
    array = [[0]*A for i in range(A)]
    print(array[1][0])
    i = 0
    j = 0
    for x in range(1, A ** 2 + 1):
        print(""+str(i)+"-"+str(j))
        array[i][j] = x
        if j+1 < A and array[i][j+1] == 0:
            j = j+1
        elif i + 1 < A and array[i+1][j] == 0:
            i = i+1
        elif j - 1 >= 0 and array[i][j-1] == 0:
            j = j-1
        elif i - 1 >= 0 and array[i-1][j] == 0:
            i = i-1
    return array


size = int(input("Enter the size of the matrix"))
matrix = generateMatrix(size)

for i in range(size):
    for j in range(size):
        print(matrix[i][j])
        print(" ")
    print("\n")