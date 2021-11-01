class ListNode {
	int val;
	ListNode next;

	ListNode(int x) {
		val = x;
		next = null;
	}
}

public class Solution {
	public ListNode swapPairs(ListNode head) {
		ListNode previous,root;
		if(head!=null&&head.next!=null){
			previous=new ListNode(-1);
			previous.next=head;
			root=head.next;
			while (head!=null&&head.next!=null) {
				previous.next=head.next;
				head.next=head.next.next;
				previous.next.next=head;
				head=head.next;
				previous=previous.next.next;
			}
			return root;
		}
		else
			return head;
	}
}