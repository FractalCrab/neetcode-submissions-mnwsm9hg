class Solution {
public:
    bool isValid(string s) {
        unordered_map <char, char> tokens = {
                {'(', ')'},
                {'[', ']'},
                {'{', '}'}
         };

        deque<char> st; 

        for (auto& ch : s){
            if (tokens.find(ch) != tokens.end()) 
                st.push_back(ch);
            else {
                if (st.empty()) return false; // didn't handle this 
                if (ch != tokens[st.back()]) return false;
                st.pop_back();
            }
        }

        return st.empty(); // this too

    }
};
