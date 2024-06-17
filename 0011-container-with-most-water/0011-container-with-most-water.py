class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)-1
        maxarea = 0
        i, j = 0, n
        while i < j:
            h = min(height[i], height[j])
            area = (j-i) * h
            maxarea = max(area, maxarea)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxarea
        