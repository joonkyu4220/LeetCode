class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        bool plus = true;
        int i = digits.size() - 1;
        while ((i >= 0) and plus)
        {
            digits[i] = (digits[i] + 1) % 10;
            plus = (digits[i] == 0);
            i -= 1;
        }
        if (digits[0] == 0)
        {
            digits.push_back(0);
            digits[0] = 1;
        }
        return digits;
    }
};
