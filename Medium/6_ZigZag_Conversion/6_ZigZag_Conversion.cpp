class Solution {
public:
    string convert(string s, int numRows) {
        int zig = numRows, zag = numRows-2, zigzag = 2*numRows-2;
        if(zigzag == 0) {
            zigsag = 1;
        }
        int groupNum = s.length()/zigzag;
        int leftOver = s.length()%zigzag;
        string padString = s;
        padString.append(zigzag - leftOver, ' ');
        char answer[1001] = "";
        int index = 0;
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j <= groupNum; j++) {
                if (i == 0) {
                    if (padString[j*zigzag] != ' '){
                        answer[index] = padString[j*zigzag];
                        index++;
                    }
                }
                else if (i == (numRows-1)) {
                    if (padString[j*zigzag + zig-1] != ' '){
                        answer[index] = padString[j*zigzag + zig-1];
                        index++;
                    }
                }
                else{
                    if (padString[j*zigzag + i] != ' '){
                        answer[index] = padString[j*zigzag + i];
                        index++;
                        if (padString[j*zigzag + zig-1 + zag - (i-1)] != ' '){
                            answer[index] = padString[j*zigzag + zig-1 + zag - (i-1)];
                            index++;
                        }
                    }
                    
                }
            }
        }
        return answer;
    }
};