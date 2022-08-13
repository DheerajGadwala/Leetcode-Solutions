class Solution {
    public boolean isHappy(int n) {
        Set<Integer> all = new HashSet<>();
        while (n != 1 && !all.contains(n)) {
            all.add(n);
            n = next(n);
        }
        return n == 1;
    }
    
    private int next(int n) {
        int next = 0;
        while (n != 0) {
            next += (n % 10) * (n % 10);
            n = (int) (n / 10);
        }
        return next;
    }
}