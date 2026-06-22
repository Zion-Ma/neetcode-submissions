class TimeMap:

    def __init__(self):
        self.records: dict[str, list] = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.records:
            self.records[key].append([value, timestamp])
        else:
            self.records[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.records:
            return ""
        l, r = 0, len(self.records[key]) - 1
        res = ""
        while l <= r:
            m = l + (r - l) // 2
            t = self.records[key][m][1]
            if t == timestamp:
                return self.records[key][m][0]
            if t > timestamp:
                r = m - 1
            else:
                l = m + 1
                res = self.records[key][m][0]
        return res


        
