class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
            if d[i] > 1:
                return i