class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
        Arrays.sort(tokens);
        int i = 0, j = tokens.length - 1, score = 0, ans = 0;
        while (i <= j) {
            if (power >= tokens[i]) {
                power -= tokens[i++];
                score++;
            }
            else if (score > 0){
                power += tokens[j--];
                score--;
            }
            else {
                break;
            }
            ans = Math.max(ans, score);
        }
        return ans;
    }
}