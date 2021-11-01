import java.util.Collections;
import java.util.List;

public class TwoDirectionSearch {
	public int largestRectangleArea(List<Integer> height) {
		if(height!=null&&height.size()!=0){
			int left, right,h,area=Collections.max(height),size;
			for (int i = 0; i < height.size(); i++) {
				h=height.get(i);
				left=i;
				right=i;
				while (left>=0&&height.get(left)>=h)
					left--;
				while(right<height.size()&&height.get(right)>=h)
					right++;
				size=(right-left-1)*h;
				area=area<size?size:area;
			}
			return area;
		}
		else
			return 0;
	}
}