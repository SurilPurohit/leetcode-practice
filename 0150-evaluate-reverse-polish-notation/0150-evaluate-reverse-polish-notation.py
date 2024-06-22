class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l = []
        for i in tokens:
            if i != '+' and i != '-' and i != '/' and i != '*':
                l.append(i)
            else:
                a = int(l[-1])
                l.pop()
                b = int(l[-1])
                l.pop()
                if i == '+':
                    l.append(a+b)
                elif i == '-':
                    l.append(b-a)
                elif i == '*':
                    l.append(a*b)
                else:
                    if floor(b/a) < 0:
                        l.append(ceil(b/a))
                    else:
                        l.append(floor(b/a))
            # print(l)
            # print(floor(-6/132))
        return int(l[0])
        
        