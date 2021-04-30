class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        keys = [0 for _ in range(k)]
        vals = [0 for _ in range(k)]
        for key in dic:
            val = dic[key]
            for i in range(k):
                if vals[i] < val:
                    keys[i+1:] = keys[i:-1]
                    vals[i+1:] = vals[i:-1]
                    keys[i] = key
                    vals[i] = val
                    break
        return keys
            
