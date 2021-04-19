class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        int answer = 0;
        int numsSize = nums.size();
        vector<int> diff;
        
        for(int i = 0; i < numsSize-1; i++){
            diff.push_back(nums[i+1] - nums[i]);
        }

        int positive = -1;
        for(int i = 0; i < numsSize-1; i++){
            if(positive == -1){
                if(diff[i] != 0){
                    positive = diff[i] > 0 ? 0:1;
                    answer++;
                }
            }
            else if(positive == 0){
                if(diff[i] < 0){
                    answer++;
                    positive = 1;
                }
            }
            else{
                if(diff[i] > 0){
                    answer++;
                    positive = 0;
                }
            }
        }

        return answer+1;
    }
};