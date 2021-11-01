import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}


public class Solution {
    private List<List<Integer>> result;

    public List<List<Integer>> levelOrder(TreeNode root) {
        result =new LinkedList<List<Integer>>();
        if(root!=null) {
            Queue<TreeNode> queue = new LinkedList<TreeNode>();
            queue.offer(root);
            levelOrder(queue);
        }
        return result;
    }

    public void levelOrder(Queue<TreeNode> queue) {
        List<Integer> list =new LinkedList<Integer>();
        Queue<TreeNode> next= new LinkedList<TreeNode>();
        TreeNode cur;
        if(!queue.isEmpty()) {
            while (!queue.isEmpty()) {
                cur = queue.remove();
                list.add(cur.val);
                if (cur.left != null)
                    next.add(cur.left);
                if (cur.right != null)
                    next.add(cur.right);
            }
            result.add(list);
            levelOrder(next);
        }
    }
}