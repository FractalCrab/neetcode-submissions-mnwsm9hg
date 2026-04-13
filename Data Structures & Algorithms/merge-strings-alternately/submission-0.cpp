class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int i = 0;
        int j = 0;
        int m = word1.length();
        int n = word2.length();

        string new_word;

        while (i < m || j < n){
            if (i < m && (j >= n || i <= j)) new_word += word1[i++];
            else new_word += word2[j++]; 
        }
           
        return new_word;

    }
};