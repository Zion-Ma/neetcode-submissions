class TimeMap:

    def __init__(self):
        self.records: dict[str, list] = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.records:
            self.records[key] = []
        self.records[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        result, values = "", self.records.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = l + (r - l) // 2
            if values[m][1] <= timestamp:
                result = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return result
