class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans=set(nums)
        count = 0
        val = 0
        for num in nums:
            if num-1 not in ans:
                count = 1
                while num+count in ans:
                    count +=1
                val = max(val,count)
        return val
        