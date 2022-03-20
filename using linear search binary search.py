 def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=nums1+nums2
        a.sort()
        #print(a)
        if len(a)%2==1:
            m=a[len(a)//2]
            return float(m)
        else:
            m=(a[len(a)//2]+a[(len(a)//2)-1])/2
           # print(a[len(a)//2],a[len(a)//2+1])
            return m
