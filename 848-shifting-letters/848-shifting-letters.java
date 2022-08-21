class Solution {
    public String shiftingLetters(String s, int[] shifts) {
        int n = shifts.length;
        for (int i = n - 2; i > -1; i--) {
            shifts[i] += shifts[i + 1];
            shifts[i] %= 26;
        }
        char[] ch = s.toCharArray();
        for (int i = 0; i < n; i++) {
            ch[i] = (char) ((ch[i] - 'a' + shifts[i]) % 26 + 'a');
        }
        StringBuilder ret = new StringBuilder();
        for (char c: ch) {
            ret.append(c);
        }
        return ret.toString();
    }
}