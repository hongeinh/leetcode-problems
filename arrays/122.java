// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150
class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int sum = 0;
        for (int i = 1; i < n; i++) {
            int difference = prices[i] - prices[i - 1];
            sum += Math.max(0, difference);
        }
        return sum;
    }
}