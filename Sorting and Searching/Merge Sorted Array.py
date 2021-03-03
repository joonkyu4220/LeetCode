class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        i = 0
        j = 0
        len1 = len(nums1)
        len2 = len(nums2)
        
        while(i < len1 and j < len2):
            if nums1[i] > nums2[j]:
                nums1[i], nums1[i+1:] = nums2[j], nums1[i:-1]
                j += 1
                m += 1
            i += 1
        nums1[m:] = nums2[j:]
