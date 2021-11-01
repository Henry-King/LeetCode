import java.util.ArrayDeque;
import java.util.Deque;
import java.util.List;

public class Solution {
	public int trap(List<Integer> height) {
		Deque<Integer> stack = new ArrayDeque<Integer>(height.size());
		int sum = 0, piece;
		for (int i = 0; i < height.size(); i++) {
			while (!stack.isEmpty()
					&& height.get(i) >= height.get(stack.peek())) {
				int oneBack = stack.pop();
				if (!stack.isEmpty()) {
					int twoBack = stack.peek();
					piece = (i - twoBack - 1)
							* (Math.min(height.get(i), height.get(twoBack)) - height
									.get(oneBack));
					sum += piece;
				}
			}
			stack.push(i);
		}
		return sum;
	}
}