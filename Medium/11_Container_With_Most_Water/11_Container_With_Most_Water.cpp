class Solution {
public:
    int maxArea(vector<int>& height) {
        int max = 0, temp = 0;
        int i = 0, j = height.size()-1;
        while(i != j){
            temp = min(height.at(i), height.at(j))*(j-i);
            if(temp > max){
                max = temp;
            }
            if(height.at(i) >= height.at(j)){
                j--;
            }
            else if(height.at(i) < height.at(j)){
                i++;
            }
        }
        return max;
    }
};