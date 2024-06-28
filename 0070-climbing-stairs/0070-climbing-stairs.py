class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        if(n == 1):
            return n
        for i in range(n):
            c = a + b
            a = b
            b = c
        return c