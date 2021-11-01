

public class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head != null && k != 1) {
            ListNode newHead = head, tmpHead = null, tmpTail = null, pre = null, next, lastPre = null;
            int count = 0;
            while (head != null) {
                if (count < k) {
                    next = head.next;
                    head.next = pre;
                    pre = head;
                    head = next;
                    count++;
                } else {
                    if (tmpHead == null) {
                        tmpHead = newHead;
                        newHead = pre;
                    } else {
                        tmpHead.next = pre;
                        tmpHead = tmpTail;
                    }
                    tmpTail = head;
                    count = 0;
                    lastPre = pre;
                }
            }
            if (count != k) {
                while (pre != lastPre) {
                    next = pre.next;
                    pre.next = head;
                    head = pre;
                    pre = next;
                }
                if (tmpHead != null)
                    tmpHead.next = head;
            } else {
                if (tmpHead != null)
                    tmpHead.next = pre;
                else
                    newHead = pre;
                if (tmpTail != null)
                    tmpTail.next = null;
                else
                    newHead = pre;
            }
            return newHead;
        } else
            return head;
    }
}