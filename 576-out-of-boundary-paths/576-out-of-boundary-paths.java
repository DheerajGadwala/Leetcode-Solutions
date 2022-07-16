class Solution {
    public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        cache = new HashMap<>();
        this.m = m;
        this.n = n;
        return res(startRow, startColumn, maxMove);
    }
    
    Map<Key, Integer> cache;
    int m, n, MOD = 1000000007;
    
    static class Key {
        
        int x, y, moves;
        
        Key(int x, int y, int moves) {
            this.x = x;
            this.y = y;
            this.moves = moves;
        }
        
        @Override
        public boolean equals(Object thatObject) {
            Key that = (Key) thatObject;
            return this.x == that.x && this.y == that.y && this.moves == that.moves;
        }
        
        @Override
        public int hashCode() {
            return Objects.hash(x, y, moves);
        }
    }
    
    int res(int x, int y, int moves) {
        Key k = new Key(x, y, moves);
        if (cache.containsKey(k)) {
            return cache.get(k);
        }
        else if (moves < 0) {
            return 0;
        }
        else if (x < 0 || y < 0 || x >= m || y >= n) {
            return 1;
        }
        else {
            int ret = res(x+1, y, moves-1);
            ret = (ret + res(x-1, y, moves-1))%MOD;
            ret = (ret + res(x, y+1, moves-1))%MOD;
            ret = (ret + res(x, y-1, moves-1))%MOD;
            cache.put(k, ret);
            return cache.get(k);
        }
    }
}