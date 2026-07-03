class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        std::set<int> num_set(nums.begin(), nums.end());

        int longest_sequence = 0;
        for (const int num : nums){
            int length = 1;
            while (num_set.count(num + length)){
                length += 1;
            }
            longest_sequence = std::max(longest_sequence, length);
        }

        return longest_sequence;

    }
};
