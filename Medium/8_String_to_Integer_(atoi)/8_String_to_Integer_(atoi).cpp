class Solution {
public:
    int myAtoi(string s) {
        long long  max = 2147483647, min = -2147483648;
        long long answer = 0;
        int ready = 0;//if '+' or '-' then 1
        int start = 0;//if read digit then 1
        long long negitive = 0;
        for(int i = 0; i < s.length(); i++){
            if((!isdigit(s[i]))&&(s[i] != '+')&&(s[i] != '-')&&(s[i] != ' ')){
                break;
            }
            else if(((ready == 1)||(start == 1))&&(!isdigit(s[i]))){
                break;
            }
            else{
                if(s[i] == '-'){
                    negitive = 1;
                    ready = 1;
                }
                else if(s[i] == '+'){
                    ready = 1;
                }
                else if(isdigit(s[i])){
                    answer = answer*10 + (s[i]-'0');
                    start = 1;
                }
            }
        }
        if(negitive == 1){
            answer *= (-1);
        }
        if(answer > max){
            answer = max;
        }
        else if(answer < min){
            answer = min;
        }
        return answer;
    }
};