class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # k = 2
        # for i in range(2, len(nums)):
        #     if nums[i] != nums[k-2]:
        #         nums[k] = nums[i]
        #         k += 1
        # return k


        d = {}
        k = 0
        for i in nums:
            d[i] = d.get(i, 0) + 1
            if d[i] <= 2:
                nums[k] = i
                k += 1
        return k
