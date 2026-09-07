class Solution:
    def heapify(self,nums,size,i):
        while True:
            largest = i

            left = 2*i+1
            right = 2*i+2

            if left < size and nums[left] > nums[largest]:
                largest = left

            if right < size and nums[right] > nums[largest]:
                largest = right

            if largest == i:
                break

            nums[largest],nums[i] = nums[i],nums[largest]

            i=largest 

    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range((n//2)-1,-1,-1):
            self.heapify(nums,n,i)
        
        for i in range(n-1,0,-1):
            nums[i],nums[0] = nums[0],nums[i]

            self.heapify(nums,i,0)
        return nums
        



        