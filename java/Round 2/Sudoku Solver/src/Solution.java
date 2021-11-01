import java.util.Arrays;

/**
 * Created by sy on 15/9/9.
 */
public class Solution {
    private final static int SIZE = 3;

    private class Tuple {
        boolean success;
        Triple triple;

        Tuple(boolean success, Triple triple) {
            this.success = success;
            this.triple = triple;
        }
    }

    private class Triple {
        Triple(int row, int column, char[][] matrix) {
            this.row = row;
            this.column = column;
            this.matrix = matrix;
        }

        int row;
        int column;
        char[][] matrix;
    }

    private final static char EMPTY = '.';
    private final static char START = '1';
    private final static char END = '9';

    public void solveSudoku(char[][] board) {
        Tuple tuple = solveSudoku(new Triple(-1, -1, board));
        char[][] matrix = tuple.triple.matrix;
        for (int i = 0; i < matrix.length; i++)
            for (int j = 0; j < matrix[i].length; j++)
                board[i][j] = matrix[i][j];
    }

    private Tuple solveSudoku(Triple triple) {
        if (reject(triple))
            return new Tuple(false, triple);
        else if (accept(triple))
            return new Tuple(true, triple);
        else {
            Triple cur = first(triple.matrix);
            while (cur != null) {
                Tuple tuple = solveSudoku(cur);

                if (tuple.success)
                    return tuple;
                else
                    cur = next(cur);
            }
            return new Tuple(false, triple);
        }
    }

    private boolean accept(Triple triple) {
        for (char[] row : triple.matrix)
            for (char item : row)
                if (item == EMPTY)
                    return false;
        return !reject(triple);
    }

    private boolean reject(Triple triple) {
        if (triple.row == -1 && triple.column == -1) {
            return false;
        } else {
            char target = triple.matrix[triple.row][triple.column];
            if (valid(triple.matrix[triple.row], target,triple.column)) {
                char[] column = new char[triple.matrix.length];
                for (int i = 0; i < column.length; i++)
                    column[i] = triple.matrix[i][triple.column];
                if (valid(column, target,triple.row)) {
                    int rowStart = triple.row / SIZE * SIZE;
                    int columnStart = triple.column / SIZE * SIZE;
                    char[] region = new char[triple.matrix.length];
                    int count = 0;
                    for (int i = rowStart; i < rowStart + SIZE; i++)
                        for (int j = columnStart; j < columnStart + SIZE; j++) {
                            region[count++] = triple.matrix[i][j];
                        }
                    if (valid(region, target, triple.row%SIZE*SIZE+triple.column%SIZE)) {
                        return false;
                    }
                }
            }
            return true;
        }
    }

    private Triple first(char[][] matrix) {
        int i, j;
        char[][] child = copy2dArray(matrix);
        for (i = 0; i < child.length; i++) {
            for (j = 0; j < child[i].length; j++)
                if (child[i][j] == EMPTY) {
                    child[i][j] = START;
                    return new Triple(i, j, child);
                }
        }
        return null;
    }

    private Triple next(Triple triple) {
        Triple result = null;
        if (triple != null) {
            char[][] matrix = triple.matrix;
            if (triple.row != matrix.length &&
                    triple.column != matrix[matrix.length - 1].length &&
                    triple.matrix[triple.row][triple.column] != END) {
                char[][] newMatrix = copy2dArray(triple.matrix);
                newMatrix[triple.row][triple.column]++;
                result = new Triple(triple.row, triple.column, newMatrix);
            }
        }
        return result;
    }

    private char[][] copy2dArray(char[][] matrix) {
        char[][] child = new char[matrix.length][];
        for (int i = 0; i < matrix.length; i++)
            child[i] = Arrays.copyOf(matrix[i], matrix[i].length);
        return child;
    }

    private boolean valid(char[] line, char target, int loc) {
        for(int i=0;i<line.length;i++)
            if(target == line[i] && i!=loc)
                return false;
        return true;
    }

}
