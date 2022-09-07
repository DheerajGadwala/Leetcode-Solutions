class Solution {
    public boolean checkDistances(String s, int[] distance) {
        Integer[] fo = new Integer[26];
        for (int i = 0; i < s.length(); i++) {
            int c = s.charAt(i) - 'a';
            if (fo[c] == null)
                fo[c] = i;
            else if (i - fo[c] - 1 != distance[c])
                return false;
        }
        return true;
    }
}