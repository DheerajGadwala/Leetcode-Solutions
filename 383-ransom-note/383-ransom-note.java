class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] r = new int[26], m = new int[26];
        for (int i = 0; i < ransomNote.length(); i++) {
            r[ransomNote.charAt(i) - 'a'] += 1;
        }
        for (int i = 0; i < magazine.length(); i++) {
            m[magazine.charAt(i) - 'a'] += 1;
        }
        for (int i = 0; i < 26; i++) {
            if(r[i]>m[i]) return false;
        }
        return true;
    }
}