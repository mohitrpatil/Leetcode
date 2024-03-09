class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        set1 = set(nums1)
        set2 = set(nums2)
        
        c = set1.intersection(set2)
        print(c)
        
        if len(c)>0:
            return sorted(list(c))[0]
        else:
            return -1
        