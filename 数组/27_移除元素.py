# 双向使用双指针
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if (len(nums)==0):
            return 0
        i=0
        j=len(nums)-1
        while(i<j):
            if(nums[j]==val):
                j-=1
            elif (nums[i]==val):
                nums[i]=nums[j]
                i+=1
                j-=1
            else:
                i+=1
        if(nums[j]==val):
            return j
        else:
            return j+1

# 正向的双指针
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if(len(nums)==0):
            return 0
        i=0
        j=0
        while(j<len(nums)):
            if(nums[j]!=val):
                nums[i]=nums[j]
                i+=1
            j+=1
        return i
