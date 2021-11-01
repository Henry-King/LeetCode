import java.util.*;

public class Solution {

    private Map<Integer, Collection<List<Integer>>> map = new HashMap<Integer, Collection<List<Integer>>>();
    private List<Integer> source;

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        initInput(candidates);
        return new ArrayList<List<Integer>>(combinationSum(target));
    }

    private void initInput(int[] candidates) {
        Set<Integer> integerSet = new HashSet<Integer>((int) ((float) candidates.length / 0.75F + 1.0F));
        for (int item : candidates)
            integerSet.add(item);
        source = new ArrayList<Integer>(integerSet);
        Collections.sort(source);
    }

    private Collection<List<Integer>> combinationSum(int target) {
        boolean contains = map.containsKey(target);
        if (contains) {
            return map.get(target);
        } else {
            Collection<List<Integer>> container = new HashSet<List<Integer>>();
            for (Integer item : source) {
                List<Integer> tmp;
                if (item > target)
                    break;
                else if (item == target) {
                    tmp = new ArrayList<Integer>(1);
                    tmp.add(item);
                    container.add(tmp);
                } else {
                    Collection<List<Integer>> subSum = combinationSum(target - item);
                    if (subSum.size() != 0) {
                        for (List<Integer> oneSum : subSum) {
                            if (oneSum.get(0) >= item) {
                                tmp = new ArrayList<Integer>(oneSum.size() + 1);
                                tmp.addAll(oneSum);
                                tmp.add(0, item);
                                container.add(tmp);
                            }
                        }
                    }
                }
            }
            map.put(target, container);
            return container;
        }
    }

}