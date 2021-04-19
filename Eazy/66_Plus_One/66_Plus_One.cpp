class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int s = digits.size();
        int carry = 0;
        for(int i = s-1; i >= 0; i--){
            if(i == s-1){
                digits[i] += 1;
            }
            else{
                if(carry == 0){
                    break;
                }
                digits[i] += carry;
            }
            if(digits[i] == 10){
                digits[i] = 0;
                carry = 1;
            }
            else{
                carry = 0;
            }
        }
        if(carry == 1){
            digits.insert(digits.begin(), 1);
        }

        return digits;
    }
};