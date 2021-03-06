class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> answer;
        if(nums.size() < 3){
            return answer;
        }
        sort(nums.begin(), nums.end());
        int target = 0;
        int pre;
        vector<int>::iterator start, end;
        for(vector<int>::iterator i = nums.begin(); i < nums.end()-2; i++){
            if(i == nums.begin()){
                pre = *i;
            }
            else if(*i == pre){
                continue;
            }
            pre = *i;
            target = 0 - pre;
            start = i+1, end = nums.end()-1;
            while(start < end){
                if(*start + *end > target){
                    end--;
                }
                else if(*start + *end < target){
                    start++;
                }
                else{
                    answer.push_back(vector<int>{pre,*start,*end});
                    start++;
                    while(*start == *(start-1) && start < end){
                        start++;
                    }
                    end--;
                }
            }
        }
        return answer;
    }
};