class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n,m = len(strs), len(strs[0])

        # max length with i-th element exists
        dp = [1] * m

        for i in range(1, m):
            for j in range(i):
                is_addable = True
                for k in range(n):
                    if strs[k][j] > strs[k][i]:
                        is_addable = False
                        break            
                if is_addable:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return m - max(dp)