import java.util.List;

class ListNode {
	int val;
	ListNode next;

	ListNode(int x) {
		val = x;
		next = null;
	}
}

public class Solution {
	public ListNode mergeKLists(List<ListNode> lists) {
		int middle = lists.size() / 2;
		if (middle > 0) {
			ListNode left=mergeKLists(lists.subList(0, middle));
			ListNode right=mergeKLists(lists.subList(middle, lists.size()));
			return merge(left, right);
		}
		else
			return lists.size()==0?null:lists.get(0);
	}
	
	private ListNode merge(ListNode left,ListNode right){
		if(left==null){
			if(right==null)
				return null;
			else
				return right;
		}
		else{
			if(right==null)
				return left;
			else{
				ListNode p=new ListNode(0),head=p;
				while(left!=null&&right!=null){
					if(left.val<right.val){
						p.next=new ListNode(left.val);
						left=left.next;
					}
					else{
						p.next=new ListNode(right.val);
						right=right.next;
					}
					p=p.next;
				}
				if(left!=null)
					p.next=left;
				else
					p.next=right;
				return head.next;
			}
		}
	}
}