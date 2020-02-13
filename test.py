import numpy
import random
import math
import matplotlib.pyplot as plt
import os

def main():
    #lists = [[random.randint(0, 100) for i in range(10)] for i in range(3)]
    #for lst in lists:
    #    print("Unsorted list:", *lst)
    #print("Bubble Sort:", *bubble_sort(lists[0]))
    #print("Insertion Sort:", *insertion_sort(lists[1]))
    #print("Quick Sort:", *quick_sort(lists[2]))
    print("Squares:", squares(11, 3) - 1)
    
def recursion_task(a, b, n = 0):
    if a == b:
        return n + 1
    if a < b:
        return recursion_task(a, b - a, n + 1)
    print("a =", a - (a - b), ", b =", b)
    return recursion_task(a - b, b, n + 1)


def squares(a, b, n=0, cnt=0):
    chars = list('abcdefg')
    lst = [list('0' * a) for i in range(b)]
    for i in range(a - (a - b)):
            for j in range(b):
                lst[i][j] = str(chars[cnt])
    

    if a == b:
        return n + 1
    if a < b:
        cnt += 1
        return squares(a, b - a, n + 1, cnt)

    for i in lst:
        print(*i)
    print("a =", a - (a - b), ", b =", b)
   
    return recursion_task(a - b, b, n + 1)
    

def bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def insertion_sort(nums):  
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert
    return nums

def partition(nums, low, high):  
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):  
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)
    return nums
    

def fun_1():
    pass

def lowerThanhundred():
    i = 0
    res = 0
    while res < 100:
        print(str(i)+ " " + str(res))
        i += 1
        res = 2 ** i

def randList():
    myList = []
    for i in range(random.randint(0, 100)):
        myList.append(random.randint(0, 100))
    
    res = 0
    resM = 1
    for i in myList:
        res += i
        print(i)
        resM *= i

    print(len(myList))
    
    res0 = res/len(myList)
    res0M = math.sqrt(resM)

    print("avg:" + str(res0))
    print("avg geom:" + str(res0M))

def check():
    myList = []
    for i in range(random.randint(0, 100)):
        myList.append(random.randint(0, 100))
    
    a = input('Enter number: ')
    if a in myList:
        print("Yes")
    else:
        print("No")

def numberSearch():
    myList = []
    for i in range(random.randint(0, 100)):
        myList.append(random.randint(0, 100))
    print(min(myList))

def neighbour():
    myList = []
    for i in range(random.randint(0, 100)):
        myList.append(random.randint(0, 100))
    print(myList)
    for i in range(1, len(myList)-1):
        if myList[i] > myList[i + 1] and myList[i] > myList[i - 1]:
            print(myList[i])

def task():
    myList = []
    for i in range(10):
        myList.append(random.randint(0, 100))
    print(myList)
    pos = input("Enter position: ")
    myList.remove(myList[int(pos)])
    print(myList)

def task1():
    c = 2.1
    r = 4 * 1/10000
    m = 7
    j = [4.2, 0.3, 1.7]
    for i in range(len(j)):
        h = (10 * r - j[i])/(pow(c, 2) + pow(math.e, -10))
        y = (h * m - pow(j[i], 2)) + pow((0.1 * c), 2)
        print("h =",h)
        print("y =", y, "\n")

    j = 0
    while j <= 1.7:
        j+=0.1
        h = (10 * r - j)/(pow(c, 2) + pow(math.e, -10))
        y = (h * m - pow(j, 2)) + pow((0.1 * c), 2)
        print("h1 =",h)
        print("y1 =", y, "\n")
        
    j = [9, 1.8, 15, -3]
    for i in j:
        m = 1
        while m <= 2:
            h = (10 * r - i)/(pow(c, 2) + pow(math.e, -10))
            y = (h * m - pow(i, 2)) + pow((0.1 * c), 2)
            m += 0.5
            print("h2 =",h)
            print("y2 =", y, "\n")

def task2():
    print('Task 2')
    p = int(input("Enter sum = "))
    q = int(input("Enter value = "))
    per = 0.03
    i = 0
    while p < q:
        p += p * per
        i += 1
        print('p =', p, "\nday:",  i)

if __name__ == "__main__":
    main()
    