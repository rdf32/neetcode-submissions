class Solution {
public:
    bool isValid(string s) {
        // std::set<char> openSet = {'(', '[', '{'}
        std::stack<char> stac;
        std::unordered_map<char, char> closedOpen = {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };
        for (const auto& c: s) {
            if (closedOpen.contains(c)){
                if (!stac.empty()){
                    char openChar = stac.top();
                    if (!(closedOpen[c] == openChar)){
                        return false;
                    }
                    stac.pop();
                } else {return false;}
            } else {
                stac.push(c);
            }
        }
        return stac.empty();
    }
};
