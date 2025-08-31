class Solution {
public:
    long long findTheArrayConcVal(vector<int>& nums) {
        int numsLength = nums.size();
        long long concatenationValue = 0;

        // O(n)
        for (int i = 0; i < (numsLength/2); i++) {
            concatenationValue += concatenation(nums[i], nums[numsLength-1-i]);

            if ( (i == ((numsLength/2) - 1)) && (numsLength%2 == 1) ) {
                concatenationValue += nums[i+1];
            }
        }

        return concatenationValue;
    }

    // basicly O(1)
    long long checkIntRange(int num) {
        int range = 0;

        // O(int's number of digits)
        while (num) {
            num /= 10;
            range++;
        }

        // O(log(int's number of digits))
        return pow(10, range);
    }

    // basicly O(1)
    long long concatenation(int firstValue, int secondValue) {
        return firstValue*checkIntRange(secondValue) + secondValue;
    }
};