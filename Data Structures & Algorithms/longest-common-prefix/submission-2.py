class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        main = strs[0]
        for i in range(len(main)):
            for j in range (1,len(strs)):
                if i >= len(strs[j]) or main[i] != strs[j][i]:
                    return main[:i]
                
        return main


        