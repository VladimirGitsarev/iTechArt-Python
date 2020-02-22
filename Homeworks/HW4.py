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
        elif self.count <= self.size:
            res = self.nums[self.count-3] + self.nums[self.count-2] + self.nums[self.count-1]
            self.nums.append(res)
        else:  
            raise StopIteration
        self.count += 1
        return res 
       
if __name__ == "__main__":
    iterator = TribonacciNumbers(35)
    for i in iterator:
        print(i)