class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        std::unordered_map<int, int> ind_store;

        for (int i = 0; i < nums.size(); i++) {
            if (ind_store.contains(nums[i]) && i - ind_store[nums[i]] <= k){
                return true;
            }
            ind_store[nums[i]] = i;;
        }

        return false;
    }
};