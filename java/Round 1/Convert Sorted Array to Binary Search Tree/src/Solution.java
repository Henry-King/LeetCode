import java.util.Arrays;

class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;

	TreeNode(int x) {
		val = x;
	}
}

public class Solution {
	public TreeNode sortedArrayToBST(int[] num) {
		if (num.length > 1) {
			int medium = num.length / 2;
			sortedArrayToBST(Arrays.copyOfRange(num, medium + 1, num.length));
			TreeNode root = new TreeNode(num[medium]);
			root.left = sortedArrayToBST(Arrays.copyOfRange(num, 0, medium));
			root.right = sortedArrayToBST(Arrays.copyOfRange(num, medium + 1,
					num.length));
			return root;
		} else if (num.length == 1)
			return new TreeNode(num[0]);
		else
			return null;
	}
}