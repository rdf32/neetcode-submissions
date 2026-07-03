class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        unordered_map<string, vector<string>> store;
        for (const auto& s : strs){
            string key = encode_string(s);
            store[key].push_back(s);
        }

        vector<vector<string>> result;
        for (const auto& [key, vec] : store){
            result.push_back(vec);
        }
        return result;
    }

    string encode_string(const string &str) {
        
        vector<int> encoded(26, 0);
        for (int i = 0; i < str.length(); i++){
            encoded[str[i] - 'a']++;
        }

        string key = to_string(encoded[0]);
        for (int i = 1; i < 26; i++){
            key += ',' + to_string(encoded[i]);
        }

        return key;
    }


};
