class Position{
	private enum STATE{TOP,RIGHT,BOTTOM,LEFT};
	private int size;
	private int left;
	private STATE current;
	private int[]loc=new int[]{0,-1};
	public Position(int size) {
		this.size=size;
		this.left=size;
		current=STATE.TOP;
	}
	
	public int[] next(){
		switch (current) {
		case TOP:
			loc[1]++;
			left--;
			if(left<1){
				left=--size;
				current=STATE.RIGHT;
			}
			break;
		case RIGHT:
			loc[0]++;
			left--;
			if(left<1){
				left=size;
				current=STATE.BOTTOM;
			}
			break;
		case BOTTOM:
			loc[1]--;
			left--;
			if(left<1){
				left=--size;
				current=STATE.LEFT;
			}
			break;
		case LEFT:
			loc[0]--;
			left--;
			if(left<1){
				left=size;
				current=STATE.TOP;
			}
			break;
		default:
			break;
		}
		return loc;
	}
}

public class Solution {
	public int[][] generateMatrix(int n) {
		Position position=new Position(n);
		int[][] matrix=init(n);
		int[] loc;
		for(int i=0;i<n*n;i++){
			loc=position.next();
			matrix[loc[0]][loc[1]]=i+1;
		}
		return matrix;
	}
	
	private int[][] init(int size){
		int [][] result=new int[size][];
		for(int i=0;i<size;i++)
			result[i]=new int[size];
		return result;
	}
}