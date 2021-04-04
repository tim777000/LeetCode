class Solution {
public:
    int strStr(string haystack, string needle) {
        int answer = -1;
        int hl = haystack.length(), nl = needle.length();
        if(needle == ""){
            return 0;
        }
        if(nl > hl){
            return answer;
        }
        for(int i = 0; i < hl-nl+1; i++){
            if(haystack[i] == needle[0]){
                if(haystack.compare(i, nl, needle) == 0){
                    answer = i;
                    break;
                }
            }
        }

        return answer;
    }
};