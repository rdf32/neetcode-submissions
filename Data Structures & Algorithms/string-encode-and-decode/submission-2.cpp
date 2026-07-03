class Solution {
public:

    string encode(vector<string>& strs) {
        string result;
        for (const auto& s : strs){
            result = result + to_string(s.length()) + '#' + s;
        }
        return result;
    }

    vector<string> decode(string s) {
        
        vector<string> decoded;

        int i = 0;
        while (i < s.length()){
            int j = i;
            while (s[j] != '#'){
                j++;
            }
            
            string st_len;
            for (int ind = i; ind < j; ind++){
                st_len = st_len + s[ind];
            }
            int len = std::stoi(st_len);

            string result;
            for (int ind = j+1; ind < j+1+len; ind++){
                result = result + s[ind];
            }
            decoded.push_back(result);
            i = j+1+len;
        }
        
        return decoded;
    }
};
