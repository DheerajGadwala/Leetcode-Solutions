class Solution {
    
    int[] prices;
    Map<Integer, Integer> cache;
    
    public int maxProfit(int[] prices) {
        this.prices = prices;
        cache = new HashMap<>();
        return res(0, false);
    }
    
    public int res(int pos, boolean holding) {
        if (cache.containsKey(pos * (holding ? 1 : -1))) {
            return cache.get(pos * (holding ? 1 : -1));
        }
        else if (pos == prices.length) {
            return 0;
        }
        else if (holding) {
            cache.put(pos, Math.max(prices[pos] + res(pos+1, false), res(pos+1, true)));
            return cache.get(pos);
        }
        else {
            cache.put(-pos, Math.max(-prices[pos] + res(pos+1, true), res(pos+1, false)));
            return cache.get(-pos);
        }
    }
    
}