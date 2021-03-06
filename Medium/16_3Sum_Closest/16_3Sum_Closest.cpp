class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int remaining = 0;
        int pre;
        int difference = 2147483647;
        int answer = 0;
        vector<int>::iterator start, end;
        for(vector<int>::iterator i = nums.begin(); i < nums.end()-2; i++){
            if(i == nums.begin()){
                pre = *i;
            }
            else if(*i == pre){
                continue;
            }
            pre = *i;
            remaining = target - pre;
            start = i+1, end = nums.end()-1;
            while(start < end){
                if(*start + *end > remaining){
                    if(difference > ((*start + *end) - remaining)){
                        difference = ((*start + *end) - remaining);
                        answer = *start + *end + pre;
                    }
                    end--;
                }
                else if(*start + *end < remaining){
                    if(difference > (remaining - (*start + *end))){
                        difference = (remaining - (*start + *end));
                        answer = *start + *end + pre;
                    }
                    start++;
                }
                else{
                    return target;
                }
            }
        }
        return answer;
    }
};