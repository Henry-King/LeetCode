import java.util.*;

public class Solution {
    private class Tuple {
        int start;
        List<Integer> list;

        Tuple(int start, List<Integer> list) {
            this.start = start;
            this.list = list;
        }

        @Override
        public boolean equals(Object obj) {
            if (obj instanceof Tuple) {
                Tuple tuple = (Tuple) obj;
                return list.equals(tuple.list);
            }
            return false;
        }

        @Override
        public int hashCode() {
            return list.hashCode();
        }
    }

    private Map<Integer, Collection<Tuple>> map = new HashMap<Integer, Collection<Tuple>>();
    private List<Integer> source;

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        initInput(candidates);
        List<List<Integer>> list;
        Collection<Tuple> tuples = combinationSum(target, 0);
        list = new ArrayList<List<Integer>>(tuples.size());
        for (Tuple tuple : tuples)
            list.add(tuple.list);
        return list;
    }

    private void initInput(int[] candidates) {
        source = new ArrayList<Integer>(candidates.length);
        for (int item : candidates)
            source.add(item);
        Collections.sort(source);
    }

    private Collection<Tuple> combinationSum(int target, int start) {
        boolean contains = map.containsKey(target);
        if (contains) {
            return map.get(target);
        } else {
            Collection<Tuple> container = new HashSet<Tuple>();
            int item;
            for (int i = 0; i < source.size(); i++) {
                item = source.get(i);
                List<Integer> tmp;
                if (item > target)
                    break;
                else if (item == target) {
                    tmp = new ArrayList<Integer>(1);
                    tmp.add(item);
                    Tuple tuple = new Tuple(i, tmp);
                    if(container.contains(tuple))
                        container.remove(tuple);
                    container.add(tuple);
                } else {
                    //因为target-item<target,所以不会导致target出现在map中
                    Collection<Tuple> subSum = combinationSum(target - item, start + 1);
                    if (subSum.size() != 0) {
                        List<Integer> oneSum;
                        for (Tuple tuple : subSum) {
                            if (tuple.start > i) {
                                oneSum = tuple.list;
                                tmp = new ArrayList<Integer>(oneSum.size() + 1);
                                tmp.addAll(oneSum);
                                tmp.add(0, item);
                                Tuple nextTuple = new Tuple(i, tmp);
                                if(container.contains(nextTuple))
                                    container.remove(nextTuple);
                                container.add(nextTuple);
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