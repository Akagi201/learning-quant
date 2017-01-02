class CombineLatest:
    def __init__(self):
        self.timestamps = []
        self.values = []
        
    def add(self, timestamp, key, value):
        if not self.has_same_timestamp(timestamp):
            self.timestamps.append(timestamp)
            self.values.append(self.values[-1].copy() if self.values else {})
        self.values[-1][key] = value

    def has_same_timestamp(self, timestamp):
        return self.timestamps and self.timestamps[-1] == timestamp