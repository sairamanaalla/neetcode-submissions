class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h={}
        n=len(s)
        l=0
        r=0
        ans=0
        hfreq=0
        while r < n:
            h[s[r]] = h.get(s[r],0) + 1
            hfreq = max(hfreq,h[s[r]])

            if (((r-l+1) - hfreq) > k):
                h[s[l]] -=1
                l +=1
            
            if (((r-l+1)-hfreq) <=k):
                ans = max(ans,(r-l+1))
            r +=1
        return ans




        