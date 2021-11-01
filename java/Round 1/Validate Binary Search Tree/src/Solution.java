class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;

	TreeNode(int x) {
		val = x;
	}
}

class TriTuple {
	boolean valid;
	int largest;
	int smallest;

	public TriTuple(boolean valid, int largest, int smallest) {
		this.valid = valid;
		this.largest = largest;
		this.smallest = smallest;
	}
}

public class Solution {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

	public boolean isValidBST(TreeNode root) {
		if (root != null)
			return validBST(root).valid;
		else
			return true;
	}

	private TriTuple validBST(TreeNode root) {
		if (root == null) {
			return new TriTuple(true, 0, 0);
		} else {
			TriTuple left, right;
			int largest, smallest;
			left = validBST(root.left);
			right = validBST(root.right);
			if (root.left != null) {
				if (left.valid && root.val > left.largest)
					smallest = left.smallest;
				else
					return new TriTuple(false, 0, 0);
			} else
				smallest = root.val;
			if (root.right != null) {
				if (right.valid && root.val < right.smallest)
					largest = right.largest;
				else
					return new TriTuple(false, 0, 0);
			} else
				largest = root.val;
			return new TriTuple(true, largest, smallest);
		}
	}
}
