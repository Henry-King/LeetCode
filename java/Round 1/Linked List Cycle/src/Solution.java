class ListNode {
	int val;
	ListNode next;

	ListNode(int x) {
		val = x;
		next = null;
	}
}

public class Solution {

	public static void main(String[] args) {
	}

	public boolean hasCycle(ListNode head) {
		ListNode once = head;
		if (head != null && head.next != null) {
			ListNode twice = head.next;
			while (twice.next != null && twice.next.next != null) {
				if (once == twice)
					return true;
				else {
					once = once.next;
					twice = twice.next.next;
				}
			}
		}
		return false;
	}
}
