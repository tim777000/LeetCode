public class Solution
{
    public string SortSentence(string s)
    {
        var splitString = s.Split(' ').OrderBy(x => x[x.Length-1]);
        var answer = String.Join(' ', splitString.Select(x => x.Remove(x.Length-1)));

        return answer;
    }
}