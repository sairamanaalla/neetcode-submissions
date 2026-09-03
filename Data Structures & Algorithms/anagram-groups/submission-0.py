class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        d={}
        for string in strs:
            arr = [0]*26
            for ch in string:
                arr[ord(ch)-ord('a')] +=1
            key=tuple(arr)
            if key in d:
                d[key].append(string)
            else:
                d[key] = []
                d[key].append(string)
        return list(d.values())


        