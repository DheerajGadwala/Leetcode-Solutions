class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> cnt = new HashMap<>();
        int tot = 0;
        for (int i = 0; i < t.length(); i++) {
            char c = t.charAt(i);
            cnt.put(c, cnt.getOrDefault(c, 0) + 1);
            tot++;
        }
        int i = 0, j = 0, w = tot, mn = Integer.MAX_VALUE, mn_i = -1, mn_j = -1;
        while (j < s.length()) {
            char c = s.charAt(j++);
            if (cnt.containsKey(c)) {
                cnt.put(c, cnt.get(c) - 1);
                tot--;
                if (cnt.get(c) >= 0) w--;
            }
            while (tot <= 0 && w == 0) {
                char x = s.charAt(i);
                if (!cnt.containsKey(x)) i++;
                else if (cnt.containsKey(x) && cnt.get(x) < 0) {
                    cnt.put(x, cnt.get(x) + 1);
                    tot++;
                    i++;
                }
                else break;
            }
            // System.out.println(i + " " + j + " " + cnt + " " + tot + " " + w);
            if (tot <= 0 && w == 0 && j - i < mn) {
                mn = j - i;
                mn_i = i;
                mn_j = j;
            }
                
        }
        StringBuilder ret = new StringBuilder();
        while (mn_i < mn_j) {
            ret.append(s.charAt(mn_i++));
        }
        return ret.toString();
        
    }
}