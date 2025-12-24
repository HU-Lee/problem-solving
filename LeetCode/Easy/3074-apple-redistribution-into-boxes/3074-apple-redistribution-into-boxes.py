class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        sorted_caps = list(reversed(sorted(capacity)))
        a,n = sum(apple), len(capacity)
        for i in range(n):
            a -= sorted_caps[i]
            if a <= 0:
                return i+1
        return n