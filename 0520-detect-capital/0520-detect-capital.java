class Solution {
    public boolean detectCapitalUse(String word) {
        boolean s = true, c = true, fc = word.charAt(0) - 65 < 26;
        for (int i = 1; i < word.length(); i++) {
            int x = word.charAt(i) - 65;
            s &= x >= 26;
            c &= x < 26;
        }
        return (fc && c) || s;
    }
}