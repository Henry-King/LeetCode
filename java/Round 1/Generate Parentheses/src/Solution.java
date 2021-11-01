import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Solution {
	public List<String> generateParenthesis(int n) {
		return new ArrayList<>(generate(n));
	}

	public Set<String> generate(int n) {
		if (n <= 0)
			return new HashSet<String>();
		else if (n == 1)
			return new HashSet<String>(Arrays.asList("()"));
		else {
			Set<String> originalSet = generate(n - 1);
			Set<String> completeSet = new HashSet<>();
			for (String item : originalSet) {
				completeSet.add("()" + item);
				completeSet.add(item + "()");
				int index = item.indexOf('(');
				while (index >= 0) {
					completeSet.add(item.substring(0, index + 1) + "()"
							+ item.substring(index + 1, item.length()));
					index = item.indexOf('(', index + 1);
				}
			}
			return completeSet;
		}
	}
}