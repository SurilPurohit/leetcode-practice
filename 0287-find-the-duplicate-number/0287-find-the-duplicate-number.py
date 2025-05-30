class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # d = {}
        # for i in nums:
        #     d[i] = d.get(i, 0) + 1
        #     if d[i] > 1:
        #         return i

        # two pointer
        slow = nums[0]
        fast = nums[0]
        # first loop to detect if there is a cycle in the list
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # second loop to detect if there is duplicate element
        slow2 = nums[0]
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow
        