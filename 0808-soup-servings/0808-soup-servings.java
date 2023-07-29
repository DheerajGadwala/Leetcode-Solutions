class Solution {
    
    Map<Integer, Map<Integer, Double>> cache;
    
    public double soupServings(int n) {
        cache = new HashMap<>();
        if (n > 4275) {
            return 1;
        }
        return helper(n, n);
    }
    
    public double helper(int a, int b) {
        if (cache.containsKey(a) && cache.get(a).containsKey(b)) {
            return cache.get(a).get(b);
        }
        else if (a <= 0 && b <= 0) {
            return 0.5;
        }
        else if (a <= 0) {
            return 1.0;
        }
        else if (b <= 0) {
            return 0.0;
        }
        else {
            double ans = 0.25*helper(a-100, b) + 0.25*helper(a-75, b-25) + 0.25*helper(a-50, b-50) + 0.25*helper(a-25, b-75);
            if (!cache.containsKey(a)) {
                cache.put(a, new HashMap<>());
            }
            cache.get(a).put(b, ans);
            return ans;
        }
    }
}