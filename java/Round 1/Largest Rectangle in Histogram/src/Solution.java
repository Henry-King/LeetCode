import java.util.ArrayDeque;
import java.util.Deque;
import java.util.List;

public class Solution {
	public int largestRectangleArea(List<Integer> height) {
		int area = 0;
		Deque<Integer> stack = new ArrayDeque<Integer>(height.size());
		for (int i = 0; i <= height.size(); i++) {
			while (!stack.isEmpty()
					&& (i == height.size() || height.get(i) < height.get(stack
							.peek()))) {
				int h = height.get(stack.pop());
				area = Math.max(area,
						h * (stack.isEmpty() ? i : i - stack.peek() - 1));
			}
			stack.push(i);
		}
		return area;
	}
}
