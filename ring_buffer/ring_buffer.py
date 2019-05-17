class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity


  def append(self, item):
    if self.current > self.capacity:
      self.current = self.current +1

      self.storage.append(item)

    if self.current == self.capacity:
      #del self.storage[]

      self.current = self.current +1

      self.storage.append(item)



  def get(self):
    pass



# -----------------------------------------

buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']