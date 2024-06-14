class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''
        letter = [l for l in s if l.isalnum()]
        for i in letter:
            st += i
        st = st.lower()
        st1 = st[::-1]
        print(st1)
        if st == st1:
            return True
        else:
            return False