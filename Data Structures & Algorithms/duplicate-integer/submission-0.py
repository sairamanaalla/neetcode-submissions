class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans=dict()
        n=len(nums)
        for i in range(n):
            if  nums[i] in ans:
                return True
            else:
                ans[nums[i]]=1

        return False
        