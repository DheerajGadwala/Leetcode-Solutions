class Solution {
    public int garbageCollection(String[] garbage, int[] travel) {
        int n = garbage.length, ans = 0; 
        Set<Character> s = new HashSet<>();
        for (int i = n - 1; i > 0; i--) {
            for (char c: garbage[i].toCharArray()) {
                s.add(c);
                ans++;
            }
            ans += s.size() * travel[i - 1];
        }
        return ans + garbage[0].length();
    }
}