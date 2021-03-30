class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        r = 0
        for i in range(31, -1, -1):
            r |= (n & 1) << i
            n >>= 1
        return r
