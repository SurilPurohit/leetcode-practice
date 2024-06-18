class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        l = set()
        i = 0 
        for j in range(len(s)):
            while s[j] in l:
                l.remove(s[i])
                i += 1
            l.add(s[j])
            max_length = max(max_length, j - i + 1)

            
            # for j in range(i, len(s)):
            #     if s[j] in l:
            #         l = []
            #     l.append(s[j])
            #     max_length = max(len(l), max_length)
                
        return max_length
        