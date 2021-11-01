import java.util.HashSet;
import java.util.Set;

public class Solution {
    private Set<Character> set = new HashSet<Character>(((int) ((float) 10 / 0.75F + 1.0F)));
    private final static int SIZE = 3;
    private final static char EMPTY = '.';

    public boolean isValidSudoku(char[][] board) {
        if (validRow(board))
            if (validColumn(board))
                if (validRegion(board))
                    return true;
        return false;
    }

    private boolean validRow(char[][] board) {
        for (char[] line : board)
            if (!valid(line))
                return false;
        return true;
    }

    private boolean validColumn(char[][] board) {
        char[] column;
        for (int j = 0; j < board.length; j++) {
            column = new char[board.length];
            for (int i = 0; i < column.length; i++)
                column[i] = board[i][j];
            if (!valid(column))
                return false;
        }
        return true;
    }

    private boolean validRegion(char[][] board) {
        int rowStart, columnStart, count;
        char[] region;
        for (int m = 0; m < SIZE; m++)
            for (int n = 0; n < SIZE; n++) {
                rowStart = m * SIZE;
                columnStart = n * SIZE;
                region = new char[SIZE * SIZE];
                count = 0;
                for (int i = rowStart; i < rowStart + SIZE; i++)
                    for (int j = columnStart; j < columnStart + SIZE; j++) {
                        region[count++] = board[i][j];
                    }
                if (!valid(region))
                    return false;
            }
        return true;
    }

    private boolean valid(char[] line) {
        set.clear();
        for (char item : line) {
            if (set.contains(item) && item != EMPTY)
                return false;
            else
                set.add(item);
        }
        return true;
    }
}