/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public bool IsSymmetricTree(TreeNode p, TreeNode q) {
        if (p == null && q == null)
        {
            return true;
        }
        else if (p != null && q != null)
        {
            if (p.val != q.val)
            {
                return false;
            }
            else
            {
                return IsSymmetricTree(p.left, q.right) && IsSymmetricTree(p.right, q.left);
            }
        }
        else
        {
            return false;
        }
    }
    public bool IsSymmetric(TreeNode root) {
        if (root == null)
        {
            return true;
        }
        else
        {
            return IsSymmetricTree(root.left, root.right);
        }
    }
}