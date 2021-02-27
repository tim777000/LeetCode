class Solution {
public:
    string longestPalindrome(string s) {
        int palindromicDPTable[1024][1024] = {{0}};
        int j = 0;
        for (int len = 1; len <= s.length(); len++){
            for (int i = 0; i < s.length(); i++){
                j = i + len - 1;
                if(j >= s.length()){
                    break;
                }
                if(len == 1){
                    palindromicDPTable[i][j] = 1;
                }
                else if(len == 2){
                    if(s[i] == s[j]){
                        palindromicDPTable[i][j] = 1;
                    }
                }
                else{
                    if((palindromicDPTable[i+1][j-1] == 1) && (s[i] == s[j])){
                        palindromicDPTable[i][j] = 1;
                    }
                }
            }
        }
        int answerPosition = 0, answerLength = 1;
        int flag = 0;
        for (int len = s.length(); len >= 1; len--){
            for (int i = 0; i < s.length(); i++){
                j = i + len - 1;
                if(j >= s.length()){
                    break;
                }
                if(palindromicDPTable[i][j] == 1){
                    answerPosition = i;
                    answerLength = len;
                    flag = 1;
                    break;
                }
            }
            if(flag == 1){
                break;
            }
        }
        return s.substr(answerPosition, answerLength);
    }
};