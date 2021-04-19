class Solution {
public:
    int lengthOfLastWord(string s) {
        int i = s.length()-1;
        int flag = 0;
        int answer = 0;
        while(i >= 0){
            if(s[i] != ' '){
                if(flag == 0){
                    flag = 1;
                }
                answer++;
            }
            else{
                if(flag == 1){
                    break;
                }
            }
            i--;
        }

        return answer;
    }
};