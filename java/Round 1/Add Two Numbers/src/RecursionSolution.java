public class RecursionSolution {
	public final static int BASE = 10;

	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		return addTwoNumbers(l1, l2, 0);
	}

	private ListNode addTwoNumbers(ListNode l1, ListNode l2, int carry) {
		if (l1 == null)
			return (carry == 0 ? l2 : addTwoNumbers(new ListNode(carry), l2,
					0));
		else if (l2 == null)
			return (carry == 0 ? l1 : addTwoNumbers(l1, new ListNode(carry),
					0));
		else {
			int sum = l1.val + l2.val + carry;
			ListNode node = new ListNode(sum % BASE);
			node.next = addTwoNumbers(l1.next, l2.next, sum / BASE);
			return node;
		}
	}
}
