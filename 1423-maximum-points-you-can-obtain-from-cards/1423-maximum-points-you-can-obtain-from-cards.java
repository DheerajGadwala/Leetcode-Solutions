class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int n = cardPoints.length - k;
        int currSum = 0, total = 0, min = Integer.MAX_VALUE;
        for (int i = 0; i < cardPoints.length; i++) {
            if (i < n) {
                currSum += cardPoints[i];
            }
            else {
                currSum -= cardPoints[i-n] - cardPoints[i];
            }
            if (i >= n - 1) {
                min = Math.min(min, currSum);
            }
            total += cardPoints[i];
        }
        return total - min;
    }
}