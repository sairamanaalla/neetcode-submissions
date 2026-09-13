class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n=len(height)
        l=0
        h=n-1
        left_max = 0
        right_max = 0
        while l < h:
            if height[l] <= height[h]:
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    ans += (left_max - height[l])
                l +=1
            else:
                if height[h]>= right_max:
                    right_max = height[h]
                else:
                    ans += (right_max - height[h])
                h -=1
        return ans


        