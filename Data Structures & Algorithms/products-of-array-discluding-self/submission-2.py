class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans = []
        lst=[1]*n
        pre = 1
        val = 1
        for i in range(n-1,-1,-1):
            val *= nums[i]
            lst[i]=val
        for i in range(n-1):
            ans.append(pre*lst[i+1])
            pre *=nums[i]
        ans.append(pre)
        return ans

        