import java.util.Arrays;

public class SortSearchSolution {
	public int[] twoSum(int[] numbers, int target) {
		int start = 0, end = 0, temp;
		int[] back = Arrays.copyOf(numbers, numbers.length);
		int[] reslut = new int[] { 0, 0 };
		Arrays.sort(back);
		for (int i = 0; i < back.length; i++) {
			start = Arrays.binarySearch(back, target - back[i]);
			if (start > 0 && start != i) {
				start = back[start];
				end = back[i];
				break;
			}
		}
		for (int i = 0; i < numbers.length; i++)
			if (numbers[i] == start) {
				reslut[0] = i + 1;
				break;
			}
		for(int i=0;i<numbers.length;i++)
			if(numbers[i]==end&&i!=reslut[0]-1){
				reslut[1]=i+1;
				break;
			}
		if (reslut[0] > reslut[1]) {
			temp = reslut[0];
			reslut[0] = reslut[1];
			reslut[1] = temp;
		}
		return reslut;
	}
}