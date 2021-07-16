class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> m;
        m[target - nums[0]] = 0;
        for (int i = 1; i< nums.size(); i++)
        {
            if (m.find(nums[i]) == m.end())
                m[target - nums[i]] = i;
            else
                return vector<int> {m[nums[i]], i};
        }
        return vector<int> {-1, -1};
    }
};
