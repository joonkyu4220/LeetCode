class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        dic = {}
        
        for n in nums1:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        
        intersection = list()
        
        for n in nums2:
            if n in dic and dic[n] > 0:
                intersection.append(n)
                dic[n] -= 1
        
        return intersection
