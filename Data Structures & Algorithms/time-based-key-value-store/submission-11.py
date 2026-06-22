class TimeMap:

    def __init__(self):
        self.records = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.records:
            self.records[key] = []
        self.records[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.records or timestamp < self.records[key][0][1]:
            return ""
        l, r = 0, len(self.records[key]) - 1
        res = 0
        while l <= r:
            m = l + (r - l) // 2
            if self.records[key][m][1] == timestamp:
                return self.records[key][m][0]
            if self.records[key][m][1] > timestamp:
                r = m - 1
            else:
                res = max(res, m)
                l = m + 1
        return self.records[key][res][0]
        
