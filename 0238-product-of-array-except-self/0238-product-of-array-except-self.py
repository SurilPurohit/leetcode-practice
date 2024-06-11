class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        count = 0
        total_zero = 1
        flag = 1
        l = []
        for i in nums:
            if i != 0:
                total *= i
            if i == 0:
                count += 1
                total_zero *= i
                flag = 0
        i = 0
        print(count)
        while i < len(nums):
            if count > 1:
                l.append(0)
            elif nums[i] == 0: 
                l.append(total)            
            elif flag == 0:
                l.append(total_zero//nums[i])
            else:
                l.append(total//nums[i])
            i += 1
        return l
            
            