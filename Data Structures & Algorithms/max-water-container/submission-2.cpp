class Solution {
public:
    int maxArea(vector<int>& heights) {
        
        int left = 0;
        int right = heights.size() - 1;

        int max_area = 0;
        while (left < right){
            int left_height = heights[left];
            int right_height = heights[right];

            int area = (right - left) * std::min(left_height, right_height);
            max_area = std::max(area, max_area);

            if (left_height <= right_height) {
                left++;
            } else {
                right--;
            }
        }
        return max_area;
    }
};
