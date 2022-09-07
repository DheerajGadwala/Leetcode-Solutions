class Solution {
    
    static int MOD = 1000000007;
    Map<Integer, Integer>[] cache;
    int endPos;
    
    public int numberOfWays(int startPos, int endPos, int k) {
        this.cache = new Map[k+1];
        this.endPos = endPos;
        return res(startPos, k);
    }
    
    private int res(int pos, int k) {
        if (cache[k] == null) cache[k] = new HashMap<>();
        if (cache[k].containsKey(pos)) {
            return cache[k].get(pos);
        }
        else if (k == 0) {
            return pos == endPos ? 1 : 0;
        }
        else {
            cache[k].put(pos, (res(pos - 1, k - 1) + res(pos + 1, k - 1))%MOD);
            return cache[k].get(pos);
        }
    }
}