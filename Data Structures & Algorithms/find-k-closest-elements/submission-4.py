class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        left = 0
        right = k

        while right < len(arr):

            if x - arr[left] > arr[right] - x:
                left += 1

            else:
                break

            right += 1

        return arr[left:left+k]