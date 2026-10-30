class Node:
    def __init__(self) -> None:
        self.time_list = []
        self.value_list = []

class TimeMap:

    def __init__(self):
        self.records = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.records:
            self.records[key] = Node()
        self.records[key].time_list.append(timestamp)
        self.records[key].value_list.append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.records:
            return ""
        res = ""
        time_list = self.records.get(key).time_list
        value_list = self.records.get(key).value_list
        left, right = 0, len(time_list) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if time_list[mid] == timestamp:
                return value_list[mid]
            if time_list[mid] > timestamp:
                right = mid - 1
            else:
                res = value_list[mid]
                left = mid + 1
        return res
        
