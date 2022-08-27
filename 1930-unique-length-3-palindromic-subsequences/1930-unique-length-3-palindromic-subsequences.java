class Solution {
    public int countPalindromicSubsequence(String s) {
        int n = s.length();
        Integer[] l = new Integer[26], r = new Integer[26];
        for (int i = 0; i < n; i++) {
            int c = s.charAt(i) - 'a';
            l[c] = l[c] == null ? i : l[c];
            r[c] = i;
        }
        Set<String> ss = new HashSet<>();
        for (int i = 0; i < 26; i++) {
            char c = (char) (i + 'a');
            if (l[i] != null)
            for (int j = l[i] + 1; j < r[i]; j++) {
                char m = s.charAt(j);
                ss.add("" + m + c);
            }
        }
        return ss.size();
    }
}

/**
class Solution {
    public int countPalindromicSubsequence(String s) {
        int n = s.length();
        Map<Character, Integer> r = new HashMap<>();
        Set<Character> l = new HashSet<>();
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            r.put(c, r.getOrDefault(c, 0) + 1);
        }
        Set<String> set = new HashSet<>();
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            r.put(c, r.get(c) - 1);
            for (char t: l) {
                if (r.get(t) > 0) {
                    set.add("" + c + t);
                }
            }
            l.add(c);
        }
        return set.size();
    }
}
**/