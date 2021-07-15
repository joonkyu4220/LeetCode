class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int xorSum = 0;
        for (int n:nums) xorSum ^= n;
        return xorSum;
    }
};
