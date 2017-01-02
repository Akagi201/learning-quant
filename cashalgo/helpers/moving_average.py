class MovingAverage:
    def __init__(self, N):
        self.N = N
        self.buffer = []
        self.tail_index = 0
        self.total = 0
        
    def add(self, v):
        if len(self.buffer) < self.N:
            self.buffer.append(v)
            self.total += v
        else:
            oldest_value = self.buffer[self.tail_index]
            self.buffer[self.tail_index] = v
            self.total += v - oldest_value
        self.tail_index += 1
        if self.tail_index == self.N:
            self.tail_index = 0
            
    def is_ready(self):
        return len(self.buffer) == self.N
            
    def get(self):
        return self.total/self.N
    
    def __repr__(self):
        return repr(self.buffer)
        