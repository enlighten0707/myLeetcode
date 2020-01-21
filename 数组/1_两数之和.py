class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        f=False
        for i in range(len(nums)):
            for j in range (i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    left=i
                    right=j
                    f=True
                    break
            if(f):
                break
        
        res=[]
        if(f==False):
            return res

        res.append(left)
        res.append(right)
        return res

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 利用哈希表/字典求解，利用两次循环
        hashMap={}
        for idx,num in enumerate(nums):
            hashMap[num]=idx
        for idx,num in enumerate(nums):
            if hashMap.get(target-num) is not None and hashMap.get(target-num) != idx:
                if idx < hashMap.get(target-num):
                    return [idx, hashMap.get(target-num)]
                else:
                    return [hashMap.get(target-num),idx]
                    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 利用哈希表/字典求解，一次循环
        hashMap={}
        for idx,num in enumerate(nums):
            if hashMap.get(target-num) is not None :
                return [hashMap.get(target-num),idx]
            hashMap[num]=idx

