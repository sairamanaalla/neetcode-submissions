class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n= len(nums)
        ans = n +1
        val = 0
        start = 0
        for i in range(n):
            val += nums[i]
            if val >= target:
                while val >= target:
                    ans = min(ans,i-start+1)
                    val -= nums[start]
                    start +=1
        if ans == n+1:
            return 0
        return ans
                
                
                

            
        