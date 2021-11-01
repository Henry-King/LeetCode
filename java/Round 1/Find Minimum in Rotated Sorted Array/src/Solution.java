import java.util.List;

public class Solution {
	public int findMin(List<Integer> nums) {
		int min=nums.get(0);
		for(int foo:nums)
			if(foo<min){
				min=foo;
				break;
			}
		return min;
	}
}