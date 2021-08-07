public class Solution {
    public int RecursiveXor(int[] nums, int answer)
    {
        if (!nums.Any())
        {
            return answer;
        }
        int element = nums[nums.Length-1];
        nums = nums.Take(nums.Length-1).ToArray();
        return RecursiveXor(nums, answer) + RecursiveXor(nums, answer ^ element);
    }
    public int SubsetXORSum(int[] nums) {
        return RecursiveXor(nums, 0);
    }
}