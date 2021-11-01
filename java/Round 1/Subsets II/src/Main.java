import java.util.List;


public class Main {

	public static void main(String[] args) {
		Solution solution=new Solution();
		List<List<Integer>> r=solution.subsetsWithDup(new int[]{1,2,2});
		System.out.println(r.toString());
	}

}
