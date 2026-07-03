class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        
        std::set<int> values;
        for (size_t i = 0; i < nums.size(); i++) {
            if (values.contains(nums[i])) {
                return true;
            };
            values.insert(nums[i]);
        }
        return false;
    }
};