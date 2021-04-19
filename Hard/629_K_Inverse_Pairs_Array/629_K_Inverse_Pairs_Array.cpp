class Solution {
public:
    int kInversePairs(int n, int k) {
        int mod = 1e9 + 7;
        long long dpTable[1024][1024] = {{0}};
        for(int i = 1; i <= n; i++){
            dpTable[i][0] = 1;
        }
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= k; j++){
                for(int l = j; l >= 0; l--){
                    if(i-1+l < j){
                        break;
                    }
                    dpTable[i][j] = (dpTable[i][j] + dpTable[i-1][l])%mod;
                }
            }
        }

        return dpTable[n][k];
    }
};