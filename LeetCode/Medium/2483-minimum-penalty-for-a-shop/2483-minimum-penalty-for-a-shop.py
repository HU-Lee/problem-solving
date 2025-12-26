class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        
        dp = [0]*(n+1)
        dp[0] = customers.count("Y")
        
        min_penalty = dp[0]
        ans = 0
        
        for i in range(1,n+1):
            if customers[i-1] == "Y":
                dp[i] = dp[i-1] - 1
            else:
                dp[i] = dp[i-1] + 1
            if dp[i] < min_penalty:
                min_penalty = dp[i]
                ans = i
        
        return ans
