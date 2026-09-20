class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = []
        n = len(arr)
        for i in range(n):

            if len(ans) < k:
                ans.append(arr[i])
            else:
                if abs(ans[0]-x) <= abs(arr[i]-x):
                    continue
                else:
                    ans.pop(0)
                    ans.append(arr[i])
        return ans

                

        