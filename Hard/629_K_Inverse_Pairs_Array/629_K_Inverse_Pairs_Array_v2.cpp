class Solution {
public:
    int kInversePairs(int n, int k) {
        int mod = 1e9 + 7;
        long long temp = 0;
        long long dpTable[1024][1024] = {{0}};
        for(int i = 1; i <= n; i++){
            for(int j = 0; j <= k; j++){
                if(j == 0){
                    dpTable[i][0] = 1;
                }
                else{
                    temp = (dpTable[i-1][j] - (j >= i? dpTable[i-1][j-i]:0) + mod)%mod;
                    dpTable[i][j] = (dpTable[i][j-1] + temp)%mod;
                }
            }
        }
        
        temp = (k == 0? 0:dpTable[n][k-1]);
        
        return (dpTable[n][k]-temp + mod)%mod;
    }
};