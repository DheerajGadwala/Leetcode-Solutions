class Solution {
    
    Integer[][] cache;
    List<List<Integer>> piles;
    int m;
    
    private int res(int pos, int rem) {
        if (rem < 0) {
            return Integer.MIN_VALUE;
        }
        else if (pos == m || rem == 0) {
            return 0;
        }
        else if (cache[pos][rem] != null) {
            return cache[pos][rem];
        }
        else {
            List<Integer> pile = piles.get(pos);
            int n = pile.size();
            int max = res(pos+1, rem);
            for (int i = 0; i < n; i++) {
                max = Math.max(max, pile.get(i) + res(pos + 1, rem - i - 1));
            }
            cache[pos][rem] = max;
            return max;
        }
    }
    
    public int maxValueOfCoins(List<List<Integer>> piles, int k) {
        this.m = piles.size();
        this.piles = piles;
        this.cache = new Integer[m][k+1];
        for (List<Integer> pile: piles) {
            int n = pile.size();
            for (int i = 1; i < n; i++) {
                pile.set(i, pile.get(i) + pile.get(i-1));
            }
        }
        return res(0, k);
    }
}