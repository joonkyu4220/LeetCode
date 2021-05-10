class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        mid = (r + l) / 2
        
        while True:
            left = nums[l]
            middle = nums[mid]
            right = nums[r]
            if left == target:
                return l
            elif middle == target:
                return mid
            elif right == target:
                return r
            
            if mid == l:
                return -1
            
            if left < middle < right:
                if middle > target:
                    r = mid - 1
                else:
                    l = mid + 1
            elif right < left < middle:
                if left < target < middle:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if middle < target < right:
                    l = mid + 1
                else:
                    r = mid - 1
            mid = (l + r) // 2
        
        
