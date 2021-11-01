public class IterativeSolution {
	public final static int BASE = 10;

	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		int sum, low, overflow = 0;
		ListNode node = new ListNode(0), head = node;
		while (l1 != null || l2 != null) {
			sum = (l1 == null ? 0 : l1.val) + (l2 == null ? 0 : l2.val)
					+ overflow;
			low = sum % BASE;
			overflow = sum / BASE;
			node.next = new ListNode(low);
			node = node.next;
			l1 = l1 == null ? null : l1.next;
			l2 = l2 == null ? null : l2.next;
		}
		if (overflow > 0)
			node.next = new ListNode(overflow);
		return head.next;
	}
}