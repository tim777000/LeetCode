public class Solution
{
    public bool IsCovered(int[][] ranges, int left, int right)
    {
        int[] checkTable = new int[51];
        foreach (var singleElements in ranges)
        {
            Array.Fill(checkTable, 1, singleElements[0], (singleElements[1]-singleElements[0]+1));
        }
        for (int i = left; i <= right; i++)
        {
            if (checkTable[i] != 1)
            {
                return false;
            }
        }
        return true;
    }
}