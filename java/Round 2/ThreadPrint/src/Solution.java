import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * Created by sy on 15/9/24.
 */
public class Solution {
    public void solution(String input) {

        ExecutorService service = Executors.newSingleThreadExecutor();
        List<Runnable> runnableList = generateRunable(input);
        while (true) {
            for (int i = 0; i < runnableList.size(); i++) {
                service.submit(runnableList.get(i));
            }
        }
    }

    private List<Runnable> generateRunable(final String input) {
        List<Runnable> runnableList = new ArrayList<Runnable>(input.length());
        for (int i = 0; i < input.length(); i++) {
            final int finalI = i;
            runnableList.add(new Runnable() {
                @Override
                public void run() {
                    System.out.print(input.charAt(finalI));
                }
            });
        }
        return runnableList;
    }
}
