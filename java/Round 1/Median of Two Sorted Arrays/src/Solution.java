
public class Solution {
	public double findMedianSortedArrays(int A[], int B[]) {
		int length=A.length+B.length;
		if(length%2==1)
			return findMedianSortedArrays(A, 0, A.length, B, 0, B.length, length/2+1);
		else
			return (findMedianSortedArrays(A, 0, A.length, B, 0, B.length, length/2)+findMedianSortedArrays(A, 0, A.length, B, 0, B.length, length/2+1))/2;
	}
	
	public double findMedianSortedArrays(int A[],int aStart,int aEnd, int B[],int bStart,int bEnd,int length){
		if((aEnd-aStart)>(bEnd-bStart))
			return findMedianSortedArrays(B,bStart,bEnd,A,aStart,aEnd,length);
		if(aEnd-aStart==0)
			return B[bStart+length-1];
		if(length==1)
			return A[aStart]<B[bStart]?A[aStart]:B[bStart];
		int pa=(aEnd-aStart)<(length/2)?(aEnd-aStart):(length/2);
		int pb=length-pa;
		if(A[aStart+pa-1]==B[bStart+pb-1])
			return A[aStart+pa-1];
		else if(A[aStart+pa-1]<B[bStart+pb-1])
			return findMedianSortedArrays(A, aStart+pa, aEnd, B, bStart, bEnd, length-pa);
		else
			return findMedianSortedArrays(A, aStart, aEnd, B, bStart+pb, bEnd, length-pb);
	}
	
}