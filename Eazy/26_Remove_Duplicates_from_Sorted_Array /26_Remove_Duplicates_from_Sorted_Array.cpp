class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int pre = 0;
        int answer = 0;
        for(int i = 0; i < nums.size(); i++){
            if(i == 0){
                pre = nums[i];
                answer++;
            }
            else{
                if(nums[i] != pre){
                    pre = nums[i];
                    swap(nums[i], nums[answer]);
                    answer++;
                }
            }
        }
        return answer;
    }
};