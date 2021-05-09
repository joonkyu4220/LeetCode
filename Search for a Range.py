class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_ = len(nums)
        if len_ == 0 or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        l = 0
        r = len_ - 1
        mid = (l + r) / 2
        while target > nums[l] and target < nums[r]:
            if mid == l:
                break
            if nums[mid] < target:
                l = mid
            elif nums[mid] > target:
                r = mid
            else:
                break
            mid = (l + r) / 2
        print(nums[l], nums[mid], nums[r])
        if nums[l] != target and nums[mid] != target and nums[r] != target:
            return [-1, -1]
        if nums[l] == target:
            mid = l
        if nums[r] == target:
            mid = r
        lr = mid
        rl = mid
        rr = r
        ll = l
        while nums[ll] != target:
            lmid = (lr + ll) / 2
            if lmid == ll:
                ll += 1
                break
            if nums[lmid] < target:
                ll = lmid
            else:
                lr = lmid
        while nums[rr] != target:
            rmid = (rr + rl) / 2
            if rmid == rl:
                rr -= 1
                break
            if nums[rmid] > target:
                rr = rmid
            else:
                rl = rmid
                
        return [ll, rr]
