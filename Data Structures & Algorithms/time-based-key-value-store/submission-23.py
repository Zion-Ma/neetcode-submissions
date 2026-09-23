class TimeMap:

    def __init__(self):
        self.records = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.records[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # if key not in self.records:
        #     return ""
        target_list = self.records.get(key, [])
        l, r = 0, len(target_list) - 1
        ans = ""
        while l <= r:
            m = l + (r - l) // 2
            if target_list[m][1] == timestamp:
                ans = target_list[m][0]
                break
            elif target_list[m][1] > timestamp:
                r = m - 1
            else:
                ans = target_list[m][0]
                l = m + 1
        return ans
            
