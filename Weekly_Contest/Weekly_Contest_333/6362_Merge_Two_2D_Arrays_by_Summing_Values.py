class Solution {
public:
    vector<vector<int>> mergeArrays(vector<vector<int>>& nums1, vector<vector<int>>& nums2) {
        int nums1_iter = 0;
        int nums2_iter = 0;
        vector<vector<int>> answer;

        while (nums1_iter < nums1.size() || nums2_iter < nums2.size()) {
            vector<int> ans_iter;
            if (nums1_iter >= nums1.size()) {
                ans_iter = { nums2[nums2_iter][0], nums2[nums2_iter][1] };
                answer.push_back(ans_iter);
                nums2_iter++;
            }
            else if (nums2_iter >= nums2.size()) {
                ans_iter = { nums1[nums1_iter][0], nums1[nums1_iter][1] };
                answer.push_back(ans_iter);
                nums1_iter++;
            }
            else if (nums1[nums1_iter][0] == nums2[nums2_iter][0]) {
                ans_iter = { nums1[nums1_iter][0], nums1[nums1_iter][1] + nums2[nums2_iter][1] };
                answer.push_back(ans_iter);
                nums1_iter++;
                nums2_iter++;
            }
            else if (nums1[nums1_iter][0] > nums2[nums2_iter][0]) {
                ans_iter = { nums2[nums2_iter][0], nums2[nums2_iter][1] };
                answer.push_back(ans_iter);
                nums2_iter++;
            }
            else if (nums1[nums1_iter][0] < nums2[nums2_iter][0]) {
                ans_iter = { nums1[nums1_iter][0], nums1[nums1_iter][1] };
                answer.push_back(ans_iter);
                nums1_iter++;
            }
        }

        return answer;
    }
};