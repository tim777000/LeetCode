class Solution
{
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2)
    {
        double answer = 0;
        int count = 0;
        int target;
        bool isOdd;
        if((nums1.size() + nums2.size())%2 == 0)
        {
            isOdd = false;
            target = (nums1.size() + nums2.size())/2;
        }
        else
        {
            isOdd = true;
            target = (nums1.size() + nums2.size())/2 + 1;
        }
        int i = 0, j = 0;
        while(true)
        {
            count++;
            if(i < nums1.size() && j < nums2.size())
            {
                if(nums2[j] < nums1[i])
                {
                    answer = nums2[j];
                    j++;
                }
                else
                {
                    answer = nums1[i];
                    i++;
                }
            }
            else
            {
                if(i >=  nums1.size())
                {
                    answer = nums2[j];
                    j++;
                }
                else if(j >= nums2.size())
                {
                    answer = nums1[i];
                    i++;
                }
            }
            if(count == target)
            {
                break;
            }
        }
        if(!isOdd)
        {
            if(i < nums1.size() && j < nums2.size())
            {
                answer += (nums2[j] < nums1[i])? nums2[j]:nums1[i];
            }
            else
            {
                if(i >=  nums1.size())
                {
                    answer += nums2[j];
                }
                else if(j >= nums2.size())
                {
                    answer += nums1[i];
                }
            }
            return answer/2;
        }

        return answer;
    }
};