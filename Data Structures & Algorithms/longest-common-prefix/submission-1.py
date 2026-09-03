class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        main = strs[0]
        ans=""
        for i in range(len(main)):
            count=0
            for j in range (1,len(strs)):
                if i < len(strs[j]):
                    if main[i] == strs[j][i]:
                        count +=1
                    else:
                        return ans
                else:
                    return ans
            
            if count == (len(strs)-1):
                ans += main[i]
        return ans


        