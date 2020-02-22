import numpy
import random
import math
import matplotlib.pyplot as plt
import os
import base64

def main():
    #lists = [[random.randint(0, 100) for i in range(10)] for i in range(3)]
    #for lst in lists:
    #    print("Unsorted list:", *lst)
    #print("Bubble Sort:", *bubble_sort(lists[0]))
    #print("Insertion Sort:", *insertion_sort(lists[1]))
    #print("Quick Sort:", *quick_sort(lists[2]))
    #print("Squares:", recursion_task(int(input("Enter a: ")), int(input("Enter b: ")) - 1))
    #print(recursion_task0(int(input("Length: ")), int(input("Width: "))))
    #print(lst)
    nums = list(0, 1, 1)
    print(nums)

def recursion_task(a, b, n=0, prev_b=0, prev_a=0, lst = [], empt_lst = []):
    if n == 0:
        empt_lst = [list('0' * a) for i in range(b)]
    if prev_b - a == 0:    
        lst.append(prev_a - b)
        print("Cut: ", prev_a - b, "x", prev_a - b, a, b, prev_a, prev_b)
    if prev_a - b == 0:
        lst.append(prev_b - a)
        print("Cut: ", prev_b - a,"x", prev_b - a, a, b, prev_a, prev_b)
    if a < b:
        return recursion_task(a, b - a, n + 1, a, b, empt_lst=empt_lst)
    if a == b:
        lst.append(a)
        print("Cut: ", a, "x", a, a, b, prev_a, prev_b)
        draw(lst, empt_lst)
        return n + 1
    return recursion_task(a - b, b, n + 1, a, b, empt_lst=empt_lst)

def recursion_task0(a, b, n=0, prev_b=0, prev_a=0, lst = [], empt_lst = [], b64 = []):
    if n == 0:
        empt_lst = [list('0' * a) for i in range(b)]
        b64 = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)] + ['+', '/']
    if prev_b - a == 0:    
        lst.append(prev_a - b)
        print("Cut: ", prev_a - b, "x", prev_a - b, a, b, prev_a, prev_b)
    if prev_a - b == 0:
        lst.append(prev_b - a)
        print("Cut: ", prev_b - a,"x", prev_b - a, a, b, prev_a, prev_b)
    if a < b:
        return recursion_task0(a, b - a, n + 1, a, b, empt_lst=empt_lst, b64=b64)
    if a == b:
        lst.append(a)
        print("Cut: ", a, "x", a, a, b, prev_a, prev_b)
        show(lst, empt_lst)
        return n + 1
    return recursion_task0(a - b, b, n + 1, a, b, empt_lst=empt_lst, b64=b64)


def draw(lst, empt):
    b64 = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)] + ['+', '/']
    print(b64[0])
    cnt = 0
    num = 0
    check = 0
    k = 0
    try:
        for n in range(len(lst)):
            #if lst[n] == 1:
            #    break
            if check + 1 == len(empt[0]):
                st = i+1
                for k in range(st, st + lst[n]):
                    for l in range(check + 1 - lst[n-1], check + 1 - lst[n-1] + lst[n]):
                        empt[k][l] = b64[cnt]
                check = l
                j = l
                i = k
            else:
                for i in range(k, lst[n]):
                    for j in range(num, num + lst[n]):
                        empt[i][j] = b64[cnt]
                check = j
                num += lst[n]
            print('c', cnt)
            cnt += 1   
        
        for i in range(len(empt)):
            for j in range(len(empt[i])):
                if empt[i][j] == '0':
                    print('cnt', cnt)
                    empt[i][j] = b64[cnt]
                    cnt+=1
                    
    except:
        #print('except:', i+n, j-n)
        #while True:
        #    for k in range(j-n, j):
        #        for l in range(i+n, i+n+n):
        #            empt[l][k] = chars[cnt]
        #    cnt+=1
        #    i+=n
            
        #for i in range(len(empt)):
        #   for j in range(len(empt[i])):
        #        if empt[i][j] == '0':
        #            empt[i][j] = chars[cnt]
        #            cnt += 1
        print("Exception:", i, j)
    for i in empt:
        print(*i)

def show(lst, empt):
    b64 = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)] + ['+', '/']
    start_pos = 0
    cnt = -1
    check = False
    for size in lst:
        for i in range(len(empt)):
            for j in range(len(empt[i])):
                if empt[i][j] == '0':
                    start_pos = [i, j]
                    cnt += 1
                    check = True
                    break
            if check:
                check = False
                break
        for i in range(start_pos[0], start_pos[0]+lst[cnt]):
            for j in range(start_pos[1], start_pos[1]+lst[cnt]):
                empt[i][j] = b64[cnt]
    for i in empt:
        print(*i)
    

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

def tri():
    cout = 0
    prev1 = 1
    prev2 = 1
    prev3 = 1
    now = prev1 + prev2 + prev3
    a = int(input())
    if a == 1:
        print(prev1)
        cout += 1
    elif a == 2:
        print(prev1)
        cout += 1
        print(prev2)
        cout += 1
    else:
        print(prev1)
        cout += 1
        print(prev2)
        cout += 1
        print(prev3)
        cout += 1
    while True:
        if a == 1:
            break
        elif a == 2:
            break
        elif a == 3:
            break
        print(now)
        cout += 1
        if cout >= a:
            break
        prev1 = prev2
        prev2 = prev3
        prev3 = now
        now = prev1 + prev2 + prev3

if __name__ == "__main__":
    main()
    