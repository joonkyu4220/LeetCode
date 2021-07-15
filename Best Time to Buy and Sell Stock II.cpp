class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int cur = prices[0];
        int sum = 0;
        for (int i = 1; i < prices.size(); ++i)
        {
            if (prices[i] > cur) sum += prices[i] - cur;
            cur = prices[i];
        }
        return sum;
    }
};
