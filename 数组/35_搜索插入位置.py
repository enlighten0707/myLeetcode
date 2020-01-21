class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        tmp=0
        for i,num in enumerate(nums):
            if(num==target):
                return i
            if(num<target) :
                tmp+=1
        return tmp


#binary search
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if(nums[len(nums)-1]<target):
            return len(nums)
        left=0
        right=len(nums)-1
        while(left<right):
            mid=int((left+right)/2)
            if(nums[mid]<target):
                left=mid+1
            else:
                right=mid
        return left
