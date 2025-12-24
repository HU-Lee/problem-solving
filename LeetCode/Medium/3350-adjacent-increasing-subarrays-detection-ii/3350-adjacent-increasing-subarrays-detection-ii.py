class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        incs = []
        n = len(nums)
        count = 1
        last = nums[0]
        for i in range(n):
            if nums[i] > last:
                count += 1
            else:
                incs.append(count)
                count = 1
            last = nums[i]
        incs.sort()
        return max(incs[-1] // 2, incs[-2])