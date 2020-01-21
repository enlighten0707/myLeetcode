#双指针
#必须原地修改，利用O(1)额外空间

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        cnt=1
        tmp=nums[0]
        for i,num in enumerate(nums):
            if(num>tmp):
                nums[cnt]=num
                tmp=num
                cnt=cnt+1
        return cnt

# more fantastic
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums)==0) :
            return 0
        i=0
        j=0
        while(j<len(nums)):
            if(nums[i]==nums[j]):
                j+=1
            else:
                i+=1
                nums[i]=nums[j]
                
        return i+1