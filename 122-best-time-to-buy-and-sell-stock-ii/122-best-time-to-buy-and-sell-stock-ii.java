class Solution {
    
    public int maxProfit(int[] prices) {
        int totalProfit = 0, boughtPrice = prices[0];
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] <= prices[i-1]) {
                totalProfit += prices[i-1] - boughtPrice;
                boughtPrice = prices[i];
            }
        }
        totalProfit += prices[prices.length - 1] > boughtPrice ? prices[prices.length - 1] - boughtPrice : 0;
        return totalProfit;
    }
    
}