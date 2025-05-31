class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        n = len(arr)
        count = 0
        while i < n:
            if arr[i] == 0:
                arr.insert(i, 0)
                i += 2
            else:
                i += 1

        count = len(arr) - n

        for i in range(count):
            arr.pop()
    