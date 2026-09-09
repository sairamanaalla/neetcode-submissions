class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = 0
        number1 = None
        count2 = 0
        number2 = None
        for num in nums:
            if number1 == num:
                count1+=1
            elif number2 == num:
                count2+=1
            elif count1 == 0:
                number1=num
                count1 =1
            elif count2 == 0:
                number2=num
                count2=1
            else:
                count1 -=1
                count2 -=1
        
        count1=0
        count2=0

        for num in nums:
            if num == number1:
                count1 +=1
            elif num == number2:
                count2 +=1

        ans=[]
        if count1 > (len(nums)//3):
            ans.append(number1)
        if count2 > (len(nums)//3):
            ans.append(number2)
        return ans
        