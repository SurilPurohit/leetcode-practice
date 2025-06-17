class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = []
        n = len(nums)
        nums = list(set(nums))
        j = 1
        for i in range(1, n+1):
            if i in nums:
                nums.remove(i)
            else:
                nums.append(i)
        return nums