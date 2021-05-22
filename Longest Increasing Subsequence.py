class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_ = len(nums)
        if len_ == 0:
            return 0
        def findInSort(list_, num_):
            if list_[0] >= num_:
                return 0
            elif list_[-1] < num_:
                return len(list_)-1
            l = 0
            r = len(list_)-1
            mid = (l + r)/2
            while True:
                if list_[l] >= num_:
                    return l
                elif list_[l] < num_ < list_[mid]:
                    r = mid - 1
                    l += 1
                elif list_[mid] == num_:
                    return mid
                elif list_[mid] < num_ < list_[r]:
                    l = mid + 1
                    r -= 1
                elif list_[r] == num_:
                    return r
                else:
                    return r + 1
        l = [10001 for _ in range(len_)]
        l[0] = nums[0]
        count = 1
        
        
        for i in range(1, len_):
            fis = findInSort(l[:count + 1], nums[i])
            l[fis] = nums[i]
            if fis == count:
                count += 1
        return count
