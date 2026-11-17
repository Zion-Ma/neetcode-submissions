class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for ops in operations:
            if ops == '+':
                num1, num2 = record[-1], record[-2]
                record.append(num1 + num2)
            elif ops == 'C':
                record.pop()
            elif ops == 'D':
                record.append(record[-1] * 2)
            else:
                record.append(int(ops))
        return sum(record)