class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int dp[50001] = {0};
        int max = 0, tmp = 0;
        for (int i = 0; i < s.length(); i++){
            int j = i-1;
            if(i != 0){
                while(s[j] != s[i]){
                    j--;
                    if(j < 0)
                        break;
                }
            }
            if(i == 0)
                tmp = 1;
            else if(j < 0){
                tmp = dp[i-1] + 1;
            }
            else{
                tmp = min((dp[i-1] + 1), (i - j));
            }
            dp[i] = tmp;
            //cout << dp[i];
        }
        for (int i = 0; i < s.length(); i++){
            if(dp[i] >= max)
                max = dp[i];
        }
        return max;
    }
};