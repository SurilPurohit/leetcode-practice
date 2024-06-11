class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]

        overall_prod = nums[0]
        
        for i in range(1, len(nums)):
            curr_max = max(max_prod * nums[i], min_prod * nums[i], nums[i])
            curr_min = min(max_prod * nums[i], min_prod * nums[i], nums[i])
            
            overall_prod = max(overall_prod, curr_max)
            
            max_prod = curr_max
            min_prod = curr_min
            
        return overall_prod