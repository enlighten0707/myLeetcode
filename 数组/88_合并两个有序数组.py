class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #归并排序
        i=0
        j=0
        tmp=[]
        while(i<m and j<n):
            if(nums1[i]<=nums2[j]):
                tmp.append(nums1[i])
                i+=1
            else:
                tmp.append(nums2[j])
                j+=1
        if(i<m):
            for k in range(i,m):
                tmp.append(nums1[k])
        if(j<n):
            for k in range(j,n):
                tmp.append(nums2[k])
        nums1[:]=tmp[:]

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 数组nums1从后向前扫描，不用额外空间，三个指针
        if(m==0):
            nums1[:]=nums2[:]
            return
        if(n==0):
            return 
        p=m+n-1
        p1=m-1
        p2=n-1

        while(p1>=0 and p2>=0):
            if(nums1[p1]<nums2[p2]):
                nums1[p]=nums2[p2]
                p2-=1
                p-=1
            else:
                nums1[p]=nums1[p1]
                p1-=1
                p-=1
        if(p2>=0):
            nums1[:p+1]=nums2[:p2+1]

