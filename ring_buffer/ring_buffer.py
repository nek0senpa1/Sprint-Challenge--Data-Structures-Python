class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity


  def append(self, item):
    # self.storage.append(item)
    self.current = self.current +1
    self.itemNum = self.current

    if self.current <= self.capacity:
      self.storage[self.current -1] = item
    

    if self.current > self.capacity:

      self.itemNum = self.current % self.capacity
      print('item num', self.itemNum)

      if self.itemNum == 0:
        # del self.storage[len(self.storage)-1]
        self.storage[len(self.storage)-1] = item

      else:
        # del self.storage[self.itemNum -1]
        self.storage[self.itemNum -1] = item

    # else:
    #   self.storage.append(item)




  def get(self):
    selfHold = []

    for i in self.storage:
      if i is not None:
        selfHold.append(i)
        print('current',self.current)

    return selfHold



# -----------------------------------------

buffer = RingBuffer(3)

print(buffer.get())   # should return []

buffer.append('a')
buffer.append('b')
print(buffer.get())
buffer.append('c')

print(buffer.get())   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

print(buffer.get())   # should return ['d', 'b', 'c']

buffer.append('e')
print(buffer.get())
buffer.append('f')
print(buffer.get())
buffer.append('g')
print(buffer.get())
buffer.append('h')
print(buffer.get())
buffer.append('i')

print(buffer.get())   # should return ['d', 'e', 'f']

buffer.append('j')
print(buffer.get())