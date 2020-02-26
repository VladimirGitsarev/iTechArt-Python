import time
import math

class TribonacciNumbers:
    def __init__(self, s):
        self.size = s
        self.count = 0
        self.nums = [0, 0, 1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 3:
            res = self.nums[self.count]
        elif self.count < self.size:
            res = self.nums[self.count-3] + self.nums[self.count-2] + self.nums[self.count-1]
            self.nums.append(res)
        else:  
            raise StopIteration
        self.count += 1
        return res 
       
class TribonacciRow():
    def __init__(self, num):
        self.num = num
        self.count = 0
        self.prev1 = 0 
        self.prev2 = 0
        self.prev3 = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count < 3:
            return 0
        elif self.count == 3:
            return 1
        elif self.count <= self.num:
            res = self.prev1 + self.prev2 + self.prev3
            self.prev1 = self.prev2
            self.prev2 = self.prev3
            self.prev3 = res            
            return res
        else:
            raise StopIteration

class LeibnizRow():
    def __init__(self, count, expected):
        self.count = count
        self.expected = expected
        self.sum = 0
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if round(self.sum, 2) != self.expected:
            cur_num = pow(-1, self.num) / (2*self.num + 1)
            self.sum += cur_num
            self.num += 1
            if self.num == 700:
                print("Sum will never equal expected number")
                raise StopIteration
            return round(self.sum, 2)
        else:
            print("Number of terms:", self.num)
            raise StopIteration

if __name__ == "__main__":
    # Easier way
    print("Tribonacci row: ")
    iterator_t = TribonacciRow(35)
    for i in iterator_t:
        print(i)

    # Harder way
    print("Tribonacci row: ")
    iterator_t_0 = TribonacciNumbers(35)
    for i in iterator_t_0:
        print(i)
    
    iterator_L = LeibnizRow(10, float(input("Enter expected sum: ")))
    for i in iterator_L:
        print(i)