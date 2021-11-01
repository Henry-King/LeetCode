public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int x = solution.toIPAddress("172.16.254.1");
        System.out.println(Integer.toBinaryString(x));
        System.out.println(x);
    }
}
