import java.util.HashMap;
import java.util.Map;

public class MapSolution {
	public int[] twoSum(int[] numbers, int target) {
		Map<Integer, Integer> map=new HashMap<>(numbers.length*2);
		for(int i=0;i<numbers.length;i++){
			Integer company=map.get(target-numbers[i]);
			if(company==null)
				map.put(numbers[i], i);
			else
				return new int[]{company+1,i+1};
		}
		return null;
	}
}