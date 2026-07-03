class Solution {
public:
    bool isAnagram(string s, string t) {
        int len_s = s.length();
        int len_t = t.length();

        if (len_t != len_s) {
            return false;
        }

        std::vector<int> s_vec(26, 0);
        std::vector<int> t_vec(26, 0);

        for (size_t i = 0; i < len_s; i++) {
            int s_index = std::tolower(s[i]) - 'a';
            int t_index = std::tolower(t[i]) - 'a';

            s_vec[s_index] += 1;
            t_vec[t_index] += 1;
        }

        for (int i = 0; i < 26; i++) {
            if (s_vec[i] != t_vec[i]) {
                return false;
            }
        }
        return true;
    }
};
