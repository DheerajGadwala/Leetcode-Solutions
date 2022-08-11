class Solution {
    public String getHint(String secret, String guess) {
        int n = secret.length();
        int bulls = 0;
        int[] sCount = new int[10], gCount = new int[10];
        for (int i = 0; i < n; i++) {
            char s = secret.charAt(i), g = guess.charAt(i);
            if (s == g) {
                bulls += 1;
            }
            gCount[g - '0'] += 1;
            sCount[s - '0'] += 1;
        }
        int cows = 0;
        for (int i = 0; i < 10; i++) {
            cows += Math.min(gCount[i], sCount[i]);
        }
        cows -= bulls;
        return bulls+"A"+cows+"B";
    }
}