class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError('Capacity incorrect')        
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * '🍪'

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError('Exceeded Capacity') #this throws a VE if cap is exceeded
        if self.size + n > self.capacity:
            raise ValueError('Exceeded Capacity') #this throws a VE if cap is exceeded
        self._size += n #this adds cookies to the jar if capacity is not exceeded


    def withdraw(self, n):
        if self.size < n: #if we want to remove more cookies than we have
            raise ValueError("Not enough cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity
        
    @property
    def size(self):
        return self._size

