import java.util.LinkedList;
import java.util.Queue;

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

public class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        if (head == null)
            return null;
        else {
            TreeNode root = initTree(head);
            sortedListToBST(root, head);
            return root;
        }
    }

    private TreeNode initTree(ListNode head) {
        ListNode cur = head.next;
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        TreeNode root = new TreeNode(0);
        queue.offer(root);
        while (cur != null) {
            TreeNode treeNode = queue.poll();

            treeNode.left = new TreeNode(0);
            queue.offer(treeNode.left);
            cur = cur.next;

            if (cur != null) {
                treeNode.right = new TreeNode(0);
                queue.offer(treeNode.right);
                cur = cur.next;
            }
        }
        return root;
    }

    private ListNode sortedListToBST(TreeNode root, ListNode head) {
        if (root.left == null && root.right == null) {
            root.val = head.val;
            return head.next;
        } else {
            if (root.left != null)
                head =sortedListToBST(root.left, head);
            root.val = head.val;
            head =head.next;
            if (root.right != null)
                head =sortedListToBST(root.right, head);
            return head;
        }
    }
}