class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boat = 0
        while left <= right:
            weight = people[left] + people[right] if left != right else people[right]
            if weight <= limit:
                left += 1
            right -= 1
            boat += 1
        return boat