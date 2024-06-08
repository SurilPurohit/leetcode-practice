class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = []
        d = {}
        for i in strs:
            s = ''.join(sorted(i))
            if s in d:
                d[s].append(i)
            else:
                d[s] = [i]
        # print(d)
        for key in d:
            l.append(d[key])
        return l
        