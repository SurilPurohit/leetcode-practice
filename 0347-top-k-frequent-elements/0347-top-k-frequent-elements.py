class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l = []
        for i in nums:
            d[i] = d.get(i, 0) + 1
        
        f = list(d.items())
        t = sorted(f, key=lambda x: x[1], reverse=True)
        r = dict(t)
        print(r)
        for key in r:
            if k > 0:
                l.append(key)
                # if l == []:
                #     l.append(key)
            k -= 1
        return l