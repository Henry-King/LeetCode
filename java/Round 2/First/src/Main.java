import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main {

    private final static char EMPTY = '.';

    public static void main(String[] args) {
        List<Integer> list = new LinkedList<Integer>();
        Scanner scanner = new Scanner(System.in);
        int lines = Integer.valueOf(scanner.nextLine()), count = 0;
        char[] array;
        List<Integer> searchStart = new ArrayList<Integer>(4);
        for (int i = 0; i < lines; i++) {
            array = scanner.nextLine().toCharArray();
            if (array.length < 4) {
                list.add(0);
            } else {
                for (int j = 0; j < 4; j++)
                    searchStart.add(j);
                do {
                    if (
                            searchFor(array, '9', searchStart, 0) &&
                                    searchFor(array, '7', searchStart, 1) &&
                                    searchFor(array, '0', searchStart, 2) &&
                                    searchFor(array, '6', searchStart, 3))
                        count++;
                    else
                        break;
                } while (true);
                list.add(count);
                count = 0;
                searchStart.clear();
            }
        }
        out(list);
    }

    private static void out(List<Integer> list) {
        if (!list.isEmpty()) {
            System.out.print(list.get(0));
            for (int i = 1; i < list.size(); i++) {
                System.out.print('\n');
                System.out.print(list.get(i));
            }
        }
    }

    private static boolean searchFor(char[] array, char item, List<Integer> list, int index) {
        int origin = index == 0 ? list.get(index) : Math.max(list.get(index), list.get(index - 1));
        for (int i = origin; i < array.length; i++)
            if (array[i] == item) {
                array[i] = EMPTY;
                list.set(index, i + 1);
                return true;
            }
        return false;
    }

}
