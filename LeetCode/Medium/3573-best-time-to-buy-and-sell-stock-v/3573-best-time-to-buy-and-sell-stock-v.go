func maximumProfit(prices []int, k int) int64 {
	n := len(prices)
	const (
		IDLE = 0
		BUY  = 1
		SELL = 2
	)

	// ~x th day, y transactions, z state -> max revenue
	INF := int64(math.MinInt32)
	dp := make([][][]int64, n)
	for i := range dp {
		dp[i] = make([][]int64, k+1)
		for j := range dp[i] {
			dp[i][j] = []int64{INF, INF, INF}
		}
	}

	dp[0][0][IDLE] = 0
	dp[0][0][BUY] = int64(-prices[0])
	dp[0][0][SELL] = int64(prices[0])

	for i := 1; i < n; i++ {
		for j := 0; j <= k; j++ {
			price := int64(prices[i])
			dp[i][j][IDLE] = dp[i-1][j][IDLE]
			if j >= 1 {
				dp[i][j][IDLE] = max(dp[i-1][j-1][BUY]+price, dp[i-1][j-1][SELL]-price, dp[i][j][IDLE])
			}
			dp[i][j][BUY] = max(dp[i-1][j][IDLE]-price, dp[i-1][j][BUY])
			dp[i][j][SELL] = max(dp[i-1][j][IDLE]+price, dp[i-1][j][SELL])
		}
	}

    answer := dp[n-1][0][IDLE]
    for i :=1; i <= k; i++ {
        answer = max(answer, dp[n-1][i][IDLE])
    }

	return answer
}