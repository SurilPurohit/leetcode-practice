class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1]
        for i in range(0, len(nums) - 1):
            l.append(nums[i] * l[i])
        for i in range(len(nums) - 2, -1, -1):
            l[i] = l[i] * nums[i+1]
            nums[i] = nums[i+1] * nums[i]
        return l    