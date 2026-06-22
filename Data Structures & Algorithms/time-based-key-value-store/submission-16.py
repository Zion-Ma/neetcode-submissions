class TimeMap:

    def __init__(self):
        self.records: dict[str, dict[str, list]] = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.records:
            self.records[key] = dict()
            self.records[key]["value"] = [value]
            self.records[key]["timestamp"] = [timestamp]
        else:
            self.records[key]["value"].append(value)
            self.records[key]["timestamp"].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.records:
            return ""
        l, r = 0, len(self.records[key]["timestamp"]) - 1
        while l <= r:
            m = l + (r - l) // 2
            if self.records[key]["timestamp"][m] == timestamp:
                return self.records[key]["value"][m]
            if self.records[key]["timestamp"][m] > timestamp:
                r = m - 1
            else:
                l = m + 1
        return self.records[key]["value"][r] if r >= 0 else ""