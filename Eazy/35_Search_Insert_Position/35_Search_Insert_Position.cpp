class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int answer = 0;
        int LeftBound = 0, RightBound = nums.size()-1;
        while(LeftBound <= RightBound){
            answer = (LeftBound + RightBound)/2;
            if(nums[answer] == target){
                break;
            }
            else if(nums[answer] > target){
                RightBound = answer-1;
            }
            else{
                if(LeftBound == RightBound){
                    answer++;
                    break;
                }
                LeftBound = answer+1;
            }
        }

        if(answer < 0){
            answer = 0;
        }

        return answer;

    }
};