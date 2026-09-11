class Solution:
    def check(self,s,l,h):
        while l < h:
            if s[l] != s[h]:
                return False
            l +=1
            h -=1
        return True
    def validPalindrome(self, s: str) -> bool:
        l=0
        h=len(s)-1
        while l < h:
            if s[l] != s[h]:
                return self.check(s,l+1,h) or self.check(s,l,h-1)
            l +=1
            h -=1
        return True
        