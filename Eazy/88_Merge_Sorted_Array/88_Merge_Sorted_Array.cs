public class Solution {
    static void Swap<T>(ref T a, ref T b)
    {
        T temp = a;
        a = b;
        b = temp;
    }
    public void Merge(int[] nums1, int m, int[] nums2, int n)
    {
        int i = m-1, j = n-1;
        for (int k = m+n-1; k >= 0; k--)
        {
            if (j < 0)
            {
                nums1[k] = nums1[i];
                i--;
            }
            else if (i < 0)
            {
                nums1[k] = nums2[j];
                j--;
            }
            else
            {
                if (nums1[i] >= nums2[j])
                {
                    nums1[k] = nums1[i];
                    i--;
                }
                else
                {
                    nums1[k] = nums2[j];
                    j--;
                }
            }
        }
    }
}