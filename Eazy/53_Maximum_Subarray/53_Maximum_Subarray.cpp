class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int s = nums.size();
        int local_max = nums[0];
        int answer = local_max;
        
        for(int i = 1; i < s; i++){
            if(local_max + nums[i] < nums[i]){
                local_max = nums[i];
            }
            else{
                local_max += nums[i]; 
            }
            if(local_max > answer){
                answer = local_max;
            }
        }

        return answer;
    }
};