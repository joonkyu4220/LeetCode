class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> count(1001, 0);
        vector<int> ans;
        for (int n:nums1)
            count[n]++;
        for (int n:nums2)
            if (count[n])
            {
                ans.push_back(n);
                count[n]--;
            }
        return ans;
    }
};
