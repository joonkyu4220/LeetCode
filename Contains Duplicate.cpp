class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // map<int, bool> m;
        // for(auto n:nums)
        //     if (m.find(n) == m.end())
        //         m[n] = true;
        //     else
        //         return true;
        // return false;
        sort(nums.begin(), nums.end());
        int i = 0;
        while (++i < nums.size())
            if(nums[i] == nums[i-1])
                return true;
        return false;        
    }
};
