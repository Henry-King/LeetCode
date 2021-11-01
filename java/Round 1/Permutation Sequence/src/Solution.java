import java.util.ArrayList;
import java.util.List;

public class Solution {
	public static void main(String argv[]) {
		Solution solution = new Solution();
		String x = solution.getPermutation(3, 5);
		System.out.println(x);
	}

	private List<Integer> list;

	public String getPermutation(int n, int k) {
		list = new ArrayList<Integer>(n);
		for (int i = 0; i < n; i++)
			list.add(i + 1);
		return permutation(n, k-1);
	}

	private String permutation(int n, int k) {
		if (n == 1)
			return Integer.toString(list.remove(0));
		else {
			return Integer.valueOf(list.remove(k/ factorial(n - 1)))
					+ permutation(n - 1, k % factorial(n - 1));
		}
	}

	private final static int factorial(int n) {
		return n == 0 ? 1 : n * factorial(n - 1);
	}
}
