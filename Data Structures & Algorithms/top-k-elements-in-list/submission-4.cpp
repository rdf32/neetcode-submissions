class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        std::unordered_map<int, int> counts;
        for (const int num: nums){
            if (counts.find(num) != counts.end()){
                counts[num]++;
            } else {
                counts[num] = 1;
            }
        }

        std::priority_queue<std::pair<int, int>> maxHeap;
        for (const auto& [num, count] : counts){
            maxHeap.push({count, num});
        }

        vector<int> result;
        while (k > 0) {
            std::pair count_num = maxHeap.top();
            result.push_back(count_num.second);
            maxHeap.pop();
            k--;
        }
        return result;
    }
};
