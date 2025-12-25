class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        happiness.reverse()

        return sum(max(happiness[i] - i, 0) for i in range(k))