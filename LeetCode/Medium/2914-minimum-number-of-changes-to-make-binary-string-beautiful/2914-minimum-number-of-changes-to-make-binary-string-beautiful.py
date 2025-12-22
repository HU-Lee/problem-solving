class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s) // 2
        
        count = 0
        for i in range(n):
            if s[2*i] != s[2*i+1]:
                count += 1
        return count