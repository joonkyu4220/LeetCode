class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int maxIdx = nums.size();
        k %= maxIdx;
        if (k == 0) return;
        
        int start = 0;
        int curIdx = start;
        int nextIdx = start + k;
        int curTemp = nums[curIdx];
        int nextTemp;
        
        for (int dummy = 0; dummy < maxIdx; ++dummy)
        {
            nextTemp = nums[nextIdx];
            nums[nextIdx] = curTemp;
            curTemp = nextTemp;
            curIdx = (curIdx + k) % maxIdx;
            nextIdx = (nextIdx + k) % maxIdx;
            if (curIdx == start)
            {
                start += 1;
                curIdx = start;
                curTemp = nums[curIdx];
                nextIdx = start + k;
            }
        }
    }
};
