class Solution {
    
    Map<Double, Map<Integer, Double>> cache = new HashMap<>();
    
    public double myPow(double x, int n) {
        if (!cache.containsKey(x)) {
            cache.put(x, new HashMap<>());
        }
        else if (cache.get(x).containsKey(n)) {
            return cache.get(x).get(n);
        }
        if (n == 1) {
            return x;
        }
        else if (n == 0) {
            return 1;
        }
        else if (n == -1) {
            return 1/x;
        }
        else if (n % 2 == 0) {
            cache.get(x).put(n, myPow(x, n/2) * myPow(x, n/2));
            return cache.get(x).get(n);
        }
        else if (n % 2 == 1) {
            cache.get(x).put(n, myPow(x, n/2) * myPow(x, n/2+1));
            return cache.get(x).get(n);
        }
        else if (n % 2 == -1) {
            cache.get(x).put(n, myPow(x, n/2) * myPow(x, n/2-1));
            return cache.get(x).get(n);
        }
        return 0;
    }
}