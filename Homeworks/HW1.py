import random as rnd

def main():
    print(task_1(int(input("Task 1:\nEnter string lentgh: "))))
    lst = [rnd.randint(0, 10) for i in range(10)] # Create a list with random numbers
    print(task_2(lst, int(input("\nTask 2:\nNumber to search: "))))
    task_3()
    task_4(int(input("\nTask 4:\nEnter matrix size: ")))
    

def task_1(str_len):    # The method takes string length from user input
    res_str = str()
    for i in range(str_len):
        for j in range(i):
            if len(res_str) < str_len*2:    # If a string shorter than input number taking into account spaces after each number
                res_str += str(i) + " "     # Adding each number and space after it to the result string
    return res_str 

def task_2(lst, number):    # The method takes a random list and a number to search from user input
    res_str = str()
    for i in range(len(lst)):   
        if lst[i] == number:
            res_str += str(i) + " "    # Adding found position and space after it to the result string
    print("List:", *lst)
    return "Positions of '{}' number: ".format(number) + res_str if len(res_str) > 0 else "Absent"    # Return found positions if a number is found in a list

def task_3():
    matrix = list()
    print("\nTask 3:\nEnter rows of numbers\nSeparate numbers with spaces\nEnter \"end\" to stop\n")
    while True:     # While user doesn't enter an 'end' string 
        row = input("Enter a row: ")    
        if row != "end":   
            matrix.append(row.split()) # Create a list from a user input string and add a new row to the matrix
        else:
            break
    
    print("\nInput matrix:")
    for row in matrix:
        print(*row)
    
    new_matrix = [list('0' * len(matrix[0])) for i in range(len(matrix))] # Create an empty matrix of the same size as user matrix
    a0, b0, an, bn = 0, 0, 0, 0 # Variables for border numbers
    print("\nNew matrix:")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):            
            if i-1 < 0: 
                a0 = len(matrix) - 1
            else: 
                a0 = i - 1
            if j - 1 < 0: 
                b0 = len(matrix[i]) - 1
            else: 
                b0 = j - 1
            if i + 1 > len(matrix)-1: 
                an = 0
            else: 
                an= i + 1
            if j + 1 > len(matrix[i]) - 1: 
                bn = 0
            else: 
                bn = j + 1
            new_matrix[i][j]= int(matrix[a0][j])+int(matrix[an][j])+int(matrix[i][b0])+int(matrix[i][bn])

    for row in new_matrix:
        print(*row)

def task_4(n):
    a = [[0 for i in range(n)] for j in range(n)] # Create a matrix of user size
 
    i = 0 # Rows counter
    j = 0 # Cols counter
    x = 1 # Current value
    k = 0 # Border index
 
    while x <= n*n:
        a[i][j] = x 
 
        if i != j: # Exclude diagonal numbers
            a[j][i] = (a[k][k] + (n-k*2)*2) * 2 - 4 - x # Add values on non-border numbers
    
        if j != n-k-1: # Move right if still non-border number
            j += 1 
        
        elif i != n-k-1: # Move down if still non-border number
            i += 1
        
        elif x != n*n: # Go to the next border and repeat
            k += 1 
            i = j = k 
            x = a[k][k-1] 
        
        x += 1 

    for i in a: 
        print(*i)

if __name__ == "__main__":
    main()