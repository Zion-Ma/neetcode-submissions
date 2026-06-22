class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        digits[-1] += 1
        carry = 0
        for n in digits[::-1]:
            n += carry
            ans.append(n % 10)
            carry = n // 10
        if carry:
            ans.append(1)
        return ans[::-1]
