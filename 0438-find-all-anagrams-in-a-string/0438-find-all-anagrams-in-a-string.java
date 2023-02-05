class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        if (s.length() < p.length()) return new ArrayList<>();
        int[] curr_count = new int[26], p_count = new int[26];
        int m = p.length(), n = s.length();
        for (char c: p.toCharArray()) {
            p_count[c - 'a']++;
        }
        for (int i = 0; i < m - 1; i++) {
            char c = s.charAt(i);
            curr_count[c-'a']++;
        }
        List<Integer> ans = new ArrayList<>();
        for (int i = m - 1; i < n; i++) {
            char c = s.charAt(i);
            curr_count[c-'a']++;
            boolean flag = true;
            for (int j = 0; j < 26; j++) {
                flag &= curr_count[j] == p_count[j];
            }
            if (flag) ans.add(i - m + 1);
            c = s.charAt(i - m + 1);
            curr_count[c-'a']--;
        }
        return ans;
    }
}