class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = ''.join(sorted(s)) # s.sort()
        b = ''.join(sorted(t)) # t.sort()
        if a == b:
            return True
        return False
        