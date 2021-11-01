public class Solution {
    public int maxProfit(int[] prices) {
       int maxProfix=0,minPrice=Integer.MAX_VALUE;
       for(int i=0;i<prices.length;i++){
    	   minPrice=(prices[i]<minPrice)?prices[i]:minPrice;
    	   maxProfix=(prices[i]-minPrice>maxProfix)?(prices[i]-minPrice):maxProfix;
       }
       return maxProfix;
    }
}