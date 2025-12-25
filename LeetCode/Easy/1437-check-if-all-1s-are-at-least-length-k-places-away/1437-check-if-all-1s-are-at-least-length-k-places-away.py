class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if 1 not in nums:
            return True
        first = nums.index(1)
        count = 0
        for n in nums[first+1:]:
            if n == 1:
                if count < k:
                    return False
                count = 0
            else:
                count += 1
        return True