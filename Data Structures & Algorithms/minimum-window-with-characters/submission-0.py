class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m=[0]*256
        for ch in t:
            m[ord(ch)] +=1
        ans=-1
        min_len=float('inf')
        l=0
        count=0
        r=0
        while r < len(s):
            if m[ord(s[r])] > 0:
                count +=1
            m[ord(s[r])] -= 1
            while count == len(t):
                if (r-l+1) < min_len:
                    min_len = r-l+1
                    ans = l
                
                m[ord(s[l])] +=1
                if m[ord(s[l])] > 0 :
                    count -=1
                l+=1
            r +=1
        
        if ans == -1:
            return ""
        return s[ans:ans+min_len]


            
            

            

        


                
            

        