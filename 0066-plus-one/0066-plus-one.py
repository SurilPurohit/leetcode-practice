class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = "".join(str(x) for x in digits)
        i = int(s) + 1
        l = []
        # print(i)
        for j in str(i):
            l.append(int(j))
        # print(s)
        return l
        