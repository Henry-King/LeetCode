import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

public class Solution {
	public List<List<Integer>> subsetsWithDup(int[] num) {
		List<Integer> list = new ArrayList<>(num.length);
		for (int i : num)
			list.add(i);
		Collections.sort(list);
		return new LinkedList<List<Integer>>(generate(list));
	}

	public Set<List<Integer>> generate(List<Integer> num) {
		if (num.size() == 0) {
			Set<List<Integer>> set = new HashSet<List<Integer>>();
			set.add(new LinkedList<Integer>());
			return set;
		} else {
			Set<List<Integer>> set = generate(num.subList(0, num.size() - 1));
			List<List<Integer>> completeList = new ArrayList<>(set.size());
			for (List<Integer> list : set)
				completeList.add(new LinkedList<Integer>(list));
			for (List<Integer> list : completeList)
				list.add(num.get(num.size() - 1));
			set.addAll(completeList);
			return set;
		}
	}
}