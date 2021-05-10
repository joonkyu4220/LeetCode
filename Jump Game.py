class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        cur = len(nums) - 2
        if cur == - 1:
            return True
        minFlag = len(nums) - 1
        while cur >= 0:
            if cur + nums[cur] >= minFlag:
                minFlag = cur
            cur -= 1
        if minFlag == 0:
            return True
        else:
            return False
        
        
        # numNums = len(nums)
        # if numNums == 1:
        #     return True
        # possible = [0]
        # maxPoss = 0
        # numPoss = 1
        # cur = 0
        # while cur < numPoss:
        #     curPoss = possible[cur]
        #     n = nums[curPoss]
        #     if maxPoss < curPoss + n:
        #         if curPoss + n >= numNums - 1:
        #             return True
        #         possible = possible + [i for i in range(maxPoss + 1, curPoss+ n + 1)]
        #         numPoss += curPoss + n - maxPoss
        #         maxPoss = curPoss + n
        #     cur += 1
        # return False
