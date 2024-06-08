class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        num = nums[0]
        for i in range(1, len(nums)):
            if num == nums[i]:
                return True
            num = nums[i]
        return False
        