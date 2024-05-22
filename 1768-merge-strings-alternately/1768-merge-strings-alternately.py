class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ''
        i, j = 0, 0
        n = len(word1) - 1
        m = len(word2) - 1
        print(max(n, m))
        for k in range(min(n, m)+1):
            if word1[i] != ' ':
                s += word1[i]
            else:
                continue
            if word2[j] != ' ':
                s += word2[j]
            else:
                continue
            i += 1
            j += 1
            print(k)
        if n > m:
            for i in range(j, len(word1)):
                s += word1[i]
        else:
            for j in range(i, len(word2)):
                s += word2[j]
        return s