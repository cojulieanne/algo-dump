class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = list(map(float, nums1))
        nums2 = list(map(float, nums2))
        nums1.extend(nums2)
        nums1.sort()
        
        length = len(nums1)
        if(len(nums1) % 2): return(nums1[int((len(nums1)-1)/2)])
        else: return((nums1[int((len(nums1)-2)/2)] + nums1[1+int((len(nums1)-2)/2)])/2)
