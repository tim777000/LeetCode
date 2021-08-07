public class Solution
{
    public int ChalkReplacer(int[] chalk, int k)
    {
        long sum = chalk.Sum(x => (long)x);
        long kLeft = k % sum;
        int totalStudent = chalk.Length;
        int answer = 0;
        while (true)
        {
            kLeft -= chalk[answer];
            if (kLeft < 0)
            {
                break;
            }
            answer++;
            answer %= totalStudent;
        }
        return answer;
    }
}