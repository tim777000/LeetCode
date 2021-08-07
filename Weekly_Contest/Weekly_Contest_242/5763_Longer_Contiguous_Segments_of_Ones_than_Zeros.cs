public class Solution
{
    public bool CheckZeroOnes(string s)
    {
        int[] maxCon = new int[2] { 0, 0 };
        int[] con = new int[2] { 0, 0 };
        char flag = s[0];
        int index = 0;
        for (int i = 0; i < s.Length; i++)
        {
            if (s[i] != flag)
            {
                index = flag - '0';
                if (con[index] > maxCon[index])
                {
                    maxCon[index] = con[index];
                }
                con[index] = 0;
                flag = s[i];
            }
            con[s[i] - '0']++;
            if (i == s.Length - 1)
            {
                index = flag - '0';
                if (con[index] > maxCon[index])
                {
                    maxCon[index] = con[index];
                }
            }
        }

        return maxCon[1] > maxCon[0];
    }
}