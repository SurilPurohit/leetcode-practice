class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = 1
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    # print('0')
                    return [i,j]

            
            
        