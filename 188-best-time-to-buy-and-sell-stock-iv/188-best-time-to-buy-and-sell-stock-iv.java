class Solution {
    
    Map<Integer, Map<Integer, Integer>> cache;
    int[] prices;
    
    public int maxProfit(int k, int[] prices) {
        this.cache = new HashMap<>();
        this.prices = prices;
        return res(0, false, k);
    }
    
    public int res(int pos, boolean holding, int count) {
        int key = pos * (holding ? 1 : -1);
        if (!cache.containsKey(key)) {
            cache.put(key, new HashMap<>());
        }
        if (cache.containsKey(key) && cache.get(key).containsKey(count)) {
            return cache.get(key).get(count);
        }
        else if (pos == prices.length || (count == 0 && !holding)) {
            return 0;
        }
        else if (holding) {
            cache.get(key).put(count, Math.max(prices[pos] + res(pos+1, false, count), res(pos+1, true, count)));
            return cache.get(key).get(count);
        }
        else {
            cache.get(key).put(count, Math.max(-prices[pos] + res(pos+1, true, count-1), res(pos+1, false, count)));
            return cache.get(key).get(count);
        }
    }
}