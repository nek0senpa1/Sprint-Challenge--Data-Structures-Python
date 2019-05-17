class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity


  def append(self, item):
    self.storage.append(item)
    self.current = self.current +1
    self.itemNum = self.current

    # if self.current > self.capacity:
    #   self.current = self.current +1

    #   self.storage.append(item)

    # if self.current == self.capacity:
    #   #del self.storage[]

    #   self.current = self.current +1

    #   self.storage.append(item)
    
    if self.current > self.capacity:
      self.itemNum = self.current // self.capacity
      print(self.itemNum)





  def get(self):
    selfHold = []

    for i in self.storage:
      if i is not None:
        selfHold.append(i)
        print('current',self.itemNum)

    return selfHold



# -----------------------------------------

buffer = RingBuffer(3)

print(buffer.get())   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

print(buffer.get())   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

print(buffer.get())   # should return ['d', 'e', 'f']