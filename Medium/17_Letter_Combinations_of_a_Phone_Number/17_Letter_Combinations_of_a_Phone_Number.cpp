class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> answer;
        char table[4][4] = {{0}};
        int len = digits.length();
        for(int i = 0; i < len; i++){
            if(digits[i] != '7' && digits[i] != '9'){
                for(int j = 0; j < 3; j++){
                    if(digits[i] == '8'){
                        table[i][j] = 'a' + (digits[i] - '0' - 2)*3 + 1 + j;
                    }
                    else{
                        table[i][j] = 'a' + (digits[i] - '0' - 2)*3 + j;
                    }
                }
            }
            else{
                for(int j = 0; j < 4; j++){
                    if(digits[i] == '9'){
                        table[i][j] = 'a' + (digits[i] - '0' - 2)*3 + 1 + j;
                    }
                    else{
                        table[i][j] = 'a' + (digits[i] - '0' - 2)*3 + j;
                    }
                }
            }
        }
        string temp = "";
        for(int i = 0; i < 4; i++){
            if(table[0][i] != 0){
                temp += table[0][i];
                if(len == 1){
                    answer.push_back(temp);
                }
            }
            else{
                break;
            }
            for(int j = 0; j < 4 ; j++){
                if(table[1][j] != 0){
                    temp += table[1][j];
                    if(len == 2){
                        answer.push_back(temp);
                    }
                }
                else{
                    break;
                }
                for(int k = 0; k < 4; k++){
                    if(table[2][k] != 0){
                        temp += table[2][k];
                        if(len == 3){
                            answer.push_back(temp);
                        }
                    }
                    else{
                        break;
                    }
                    for(int l = 0; l < 4; l++){
                        if(table[3][l] != 0){
                            temp += table[3][l];
                            if(len == 4){
                                answer.push_back(temp);
                            }
                        }
                        else{
                            break;
                        }
                        temp.erase(3, 1);
                    }
                    temp.erase(2, 2);
                }
                temp.erase(1, 3);
            }
            temp.erase(0, 4);
        }
        return answer;
    }
};