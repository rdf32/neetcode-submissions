class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        std::sort(nums.begin(), nums.end()); // passing addresses here
        
        vector<vector<int>> results;
        for (int i = 0; i < n; i++){
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int j = i + 1;
            int k = n - 1;

            while (j < k) {
                int value = nums[i] + nums[j] + nums[k];

                if (value < 0) {
                    j++;
                } else if (value > 0) {
                    k--;
                } else {
                    results.push_back({nums[i], nums[j], nums[k]});
                    j++;
                    k--;
                    while (j < k and nums[j] == nums[j - 1]){
                        j++;
                    }
                }

            }
        }
        return results;
    }
};
