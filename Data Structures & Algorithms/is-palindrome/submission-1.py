class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        h=len(s)-1
        while l < h:
            if not (48 <= ord(s[l]) <= 57 or 65 <= ord(s[l]) <= 90 or 97 <= ord(s[l]) <= 122):
                l += 1
            elif not (48 <= ord(s[h]) <= 57 or 65 <= ord(s[h]) <= 90 or 97 <= ord(s[h]) <= 122):
                h -= 1
            elif s[l].lower() != s[h].lower():
                print(s[l]," ")
                print(s[h])
                return False
            else:
                l +=1
                h -=1
        return True
        