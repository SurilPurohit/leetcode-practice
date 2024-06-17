class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        for i in range(len(nums)):
            j, k = i+1, len(nums)-1
            while(j < k):
                if (nums[j] - nums[i] == diff) and (nums[k] - nums[j] == diff):
                    count += 1
                    j += 1
                    k -= 1
                elif (nums[j] - nums[i] < diff):
                    j += 1
                elif (nums[k] - nums[j] > diff):
                    k -= 1
                else:
                    j += 1
                    k -= 1
        return count
                    
            
        