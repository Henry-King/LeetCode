import java.util.*;

public class Main {
    private final static char LEFT = '(';
    private final static char RIGHT = ')';

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int lines = Integer.valueOf(scanner.nextLine());
        List<Long> result = new ArrayList<Long>(lines);
        for (int i = 0; i < lines; i++) {
            result.add(process(scanner.nextLine()));
        }
        out(result);
    }

    private static long process(String line) {
        long num = 0;
        int times = 0;
        Deque<Long> stack = new LinkedList<Long>();
        for (int i = 0; i < line.length(); i++) {
            if (Character.isAlphabetic(line.charAt(i)))
                num++;
            else if (Character.isDigit(line.charAt(i))) {
                times = times * 10 + (line.charAt(i) - '0');
                if (i + 1 == line.length() || !Character.isDigit(line.charAt(i + 1))) {
                    int back = Integer.toString(times).length();
                    if (Character.isAlphabetic(line.charAt(i - back))) {
                        num += times - 1;
                    } else {
                        num += stack.pop() * times;
                    }
                    times = 0;
                }
            } else if (line.charAt(i) == LEFT || line.charAt(i) == RIGHT) {
                stack.push(num);
                num = 0;
            }
        }
        while (!stack.isEmpty())
            num += stack.pop();
        return num;
    }

    private static void out(List<Long> list) {
        if (!list.isEmpty()) {
            System.out.print(list.get(0));
            for (int i = 1; i < list.size(); i++) {
                System.out.print('\n');
                System.out.print(list.get(i));
            }
        }
    }
}
