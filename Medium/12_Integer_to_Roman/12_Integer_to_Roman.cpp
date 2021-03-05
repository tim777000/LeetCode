class Solution {
public:
    string intToRoman(int num) {
        int remainder = 0;
        int remainder_temp = 0, quotient_temp = 0;
        int count = 0;
        string symbol = "IXCMVLD";
        char answer[128] = "";
        int index = 0;
        while (num != 0){
            remainder = num % 10;
            remainder_temp = remainder % 5;
            quotient_temp = remainder / 5;
            if(remainder_temp <= 3){
                for(int i = 0; i < remainder_temp; i++){
                    answer[index] = symbol[count];
                    index++;
                }
                if(quotient_temp == 1){
                    answer[index] = symbol[count+4];
                    index++;
                }
            }
            else{
                if(quotient_temp == 1){
                    answer[index] = symbol[count+1];
                    index++;
                }
                else{
                    answer[index] = symbol[count+4];
                    index++;
                }
                answer[index] = symbol[count];
                index++;
            }
            count++;
            num /= 10;
        }
        string ans_str = answer;
        reverse(ans_str.begin(), ans_str.end());
        return ans_str;
    }
};