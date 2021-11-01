
import java.util.ArrayList;
import java.util.List;

public class Solution {
    class Point {
        int x;
        int y;
    }

    private int total=0;
    private int n;

    public int totalNQueens(int n) {
        this.n = n;
        List<Point> list = new ArrayList<Point>();
        solveNQueens(list);
        return total;
    }

    private void solveNQueens(List<Point> list) {
        if (reject(list))
            ;
        else if (accept(list)) {
            total++;
        } else {
            List<Point> cur = first(list);
            while (cur != null) {
                solveNQueens(cur);
                cur = next(cur);
            }
        }
    }

    private boolean reject(List<Point> list) {
        if (list.isEmpty())
            return false;
        else {
            Point point = list.get(list.size() - 1);
            for (int i=0;i<list.size()-1;i++) {
                if (overlap(list.get(i), point))
                    return true;
            }
            return false;
        }
    }

    private boolean overlap(Point a, Point b) {
        return
                a.x == b.x ||
                        a.y == b.y ||
                        a.x + a.y == b.x + b.y ||
                        a.x - b.x == a.y - b.y;
    }

    private boolean accept(List<Point> list) {
        return list.size() == n;
    }

    private List<Point> first(List<Point> list) {
        if (list.size() < n) {
            List<Point> result = new ArrayList<Point>(list.size() + 1);
            result.addAll(list);
            Point point;
            if (result.isEmpty())
                point = new Point();
            else
                point = createPoint(result.get(result.size() - 1));
            if (point != null) {
                result.add(point);
                return result;
            } else
                return null;
        } else
            return null;

    }

    private List<Point> next(List<Point> list) {
        List<Point> result = new ArrayList<Point>(list);
        Point point = alertPoint(result.get(result.size() - 1));
        if (point != null) {
            result.set(result.size() - 1, point);
            return result;
        } else
            return null;
    }

    private Point createPoint(Point origin) {
        Point point = new Point();
        if(origin.y<n-1) {
            point.x=0;
            point.y =origin.y+1;
            return point;
        }
        else
            return null;
    }

    private Point alertPoint(Point origin){
        Point point = new Point();
        if(origin.x<n-1) {
            point.x=origin.x+1;
            point.y =origin.y;
            return point;
        }
        else
            return null;
    }

}