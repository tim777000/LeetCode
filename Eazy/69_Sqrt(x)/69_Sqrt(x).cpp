class Solution {
public:
    int mySqrt(int x) {
        x = (long long)x;
        long long lowerBound = 0, upperBound = x;
        long long answer;
        while(lowerBound < upperBound){
            answer = (lowerBound+upperBound)/2;
            if(answer*answer == x){
                break;
            }
            else if(answer*answer > x){
                upperBound = answer-1;
            }
            else{
                lowerBound = answer+1;
            }
        }
        answer = (lowerBound+upperBound)/2;
        
        if(answer*answer > x){
            answer--;
        }

        return answer;
    }
};