class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 1 and nums[0] == 1:
            return 0
        nums.sort()
        print(nums)
        i = 0
        while i < len(nums)-1:
            if nums[i+1] - nums[i] != 1:
                # print()
                return i+1
            i+=1
        return len(nums)
