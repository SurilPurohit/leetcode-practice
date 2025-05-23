class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            k = target-nums[i]
            if k in nums:   
                j = nums.index(k)
                l = i
        return [l, j]
