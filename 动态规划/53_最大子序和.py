class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 方法一：贪心算法
        maxSum=curSum=nums[0]
        for i in range(1,len(nums)):
            curSum=max(curSum+nums[i],nums[i])
            maxSum=max(maxSum,curSum)
        return maxSum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 方法二：动态规划,本质上是贪心算法的思想
        maxSum=nums[0]
        for i in range(1,len(nums)):
            nums[i]=max(nums[i],nums[i-1]+nums[i])
            maxSum=max(maxSum,nums[i])
        return maxSum
        
class Solution:
    def merge(left,right,mid,nums:List[int]):
        left_maxSum=0
        p=mid
        while(p>=left and nums[p]>=0):
            left_maxSum+=nums[p]
            p-=1
        right_maxSum=0
        p=mid+1
        while(p<=right and nums[p]>=0):
            right_maxSum+=nums[p]
            p+=1
        return left_maxSum+right_maxSum

    def maxSubArraySub(left, right, nums:List[int]):
        if(left==right):
            return nums[left]
        mid=int((left+right)/2)
        return max(maxSubArraySub(left,mid,nums),maxSubArraySub(mid+1,right,nums),merge(left,right,mid,nums))

    def maxSubArray(self, nums: List[int]) -> int:
        # 分治法
        return maxSubArraySub(0,len(nums)-1,nums)

        
