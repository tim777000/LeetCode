public class Solution {
    public int[] MemLeak(int memory1, int memory2)
    {
        int memoryUsage = 1;
        int[] answer = new int[3];
        while(true)
        {
            if (memory1 < memoryUsage && memory2 < memoryUsage)
            {
                answer[0] = memoryUsage;
                answer[1] = memory1;
                answer[2] = memory2;
                break;
            }
            if (memory1 >= memory2)
            {
                memory1 -= memoryUsage;
            }
            else{
                memory2 -= memoryUsage;
            }
            memoryUsage++;
        }
        return answer;
    }
}