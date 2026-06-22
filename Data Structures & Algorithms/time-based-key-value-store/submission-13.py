class TimeMap:

    def __init__(self):
        self.record = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.record[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not self.record[key]:
            return ""
        targetList = self.record[key]
        l, r = 0, len(targetList) - 1
        res = ""
        while l <= r:
            m = l + (r - l) // 2
            if targetList[m][0] <= timestamp:
                res = targetList[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
