class Solution:
    def isValid(self, s: str) -> bool:
        st = ''
        for i in s:
            if (i == ')' or i == ']' or i == '}') and st == '':
                return False
            elif i == ')' and st[-1] == '(':
                st = st[:-1]
            elif i == '}' and st[-1] == '{':
                st = st[:-1]
            elif i == ']' and st[-1] == '[':
                st = st[:-1]
            else:
                st += i
                
        if st == '':
            return True
        return False
        