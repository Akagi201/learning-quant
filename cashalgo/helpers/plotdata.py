import pandas

class PlotData:
    def __init__(self, interval):
        self.interval = interval
        self.timestamps = []
        self.data = []
        self.data_xy = []
        
    def add(self, timestamp, v):
        self.timestamps.append(timestamp)
        self.data.append(v)
        self.data_xy.append([timestamp, v])
        
    def get(self):
        return pandas.Series(self.data, index = self.timestamps)
    