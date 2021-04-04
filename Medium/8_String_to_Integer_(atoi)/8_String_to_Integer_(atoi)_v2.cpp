class Solution {
public:
    int myAtoi(string s) {
        long long upper = 2147483647;
        long long lower = 2147483648;
        long long answer = 0;
        bool isPos = true;
        int i = 0;
        while(i < s.length()){
            if(s[i] == '-'){
                isPos = false;
                break;
            }
            else if(s[i] == '+'){
                isPos = true;
                break;
            }
            else if(isdigit(s[i])){
                answer += s[i] - '0';
                break;
            }
            else if(s[i] == ' '){
                i++;
            }
            else{
                return 0;
            }
        }
        for (int j = i+1; j < s.length(); j++){
            if(isdigit(s[j])){
                answer = answer*10 + (s[j] - '0');
                if(isPos && answer > upper){
                    answer = upper;
                    break;
                }
                if(!isPos && answer > lower){
                    answer = lower;
                    break;
                }
            }
            else{
                break;
            }
        }

        if(!isPos){
            answer *= (-1);
        }

        return answer;
    }
};