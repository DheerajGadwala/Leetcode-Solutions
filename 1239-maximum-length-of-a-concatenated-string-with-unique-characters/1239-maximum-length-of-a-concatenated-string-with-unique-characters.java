class Solution {
    
    // Map<Integer, Map<Set<Character>, Integer>> cache;
    Map<Set<Character>, Integer> []cache;
    List<String> arr;
    int n;
    
    public int res(int pos, Set<Character> acc) {
        if (cache[pos] == null) cache[pos] = new HashMap<>();
        if (pos == n) return 0;
        if (cache[pos].containsKey(acc)) return cache[pos].get(acc);
        String curr = arr.get(pos);
        Set<Character> copy = new HashSet<>(acc);
        for (char c: curr.toCharArray()) {
            if (copy.contains(c)) {
                cache[pos].put(acc, res(pos+1, acc));
                return cache[pos].get(acc);
            }
            else
                copy.add(c);
        }
        cache[pos].put(acc, Math.max(curr.length() + res(pos+1, copy), res(pos+1, acc)));
        return cache[pos].get(acc);
    }
    
    public int maxLength(List<String> arr) {
        this.arr = arr;
        this.n = arr.size();
        this.cache = new HashMap[n+1];
        int ans = res(0, new HashSet<>());
        return ans;
    }
}