public class Main {

    public static void main(String[] args) {
        ListNode h = new ListNode(1);
        ListNode head =h;
//        for (int i = 2; i < 10; i++) {
//            h.next = new ListNode(i);
//            h = h.next;
//        }
        Solution solution = new Solution();
        ListNode r = solution.reverseKGroup(head, 3);
        System.out.println(r.val);
    }
}
