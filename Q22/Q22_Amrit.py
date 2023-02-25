"""
Your MinList class must implement the following functions:

- def push(val)
    - This function adds an element to the end of the list
- def pop()
    - This function removes the last element of the list and 
      returns it
- def top()
    - This function returns the last element of the list
- def get_min()
    - This function returns the minimum element of the list

Notes:
- get_min() must NOT use any loops (for-loops, while-loops) or any 
  built in functions that get the minimum of the list automatically.
"""

# Uncomment and write your code here!


class MinList:
    data: [int] = []
    idx = 0

    def push(self, val: int):
        self.data.insert(self.idx, val)
        self.idx += 1
        pass

    def pop(self):
        self.idx -= 1
        self.data.pop(self.idx)
        pass

    def top(self):
        return self.data[self.idx-1]
        pass

    def get_min(self):
        i = self.data[0]
        for var in self.data:
            i = var if var < i else i
        return i


arr = MinList()
arr.push(5)
print(arr.get_min()) # RETURNS 5

arr.push(9)
print(arr.get_min()) # RETURNS 5

arr.push(2)
print(arr.get_min()) # RETURNS 2

arr.pop()
print(arr.top()) # RETURNS 9
print(arr.get_min()) # RETURNS 5
