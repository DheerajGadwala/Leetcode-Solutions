class Solution {
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        
        List<String> ret = new ArrayList<>();
        
        int n = pattern.length();
        
        for (String word: words) {
            Map<Character, Character> mp = new HashMap<>(), rmp = new HashMap<>();
            boolean match = true;
            for (int i = 0; i < n; i++) {
                char a = word.charAt(i), b = pattern.charAt(i);
                if (!mp.containsKey(b) && !rmp.containsKey(a)) {
                    mp.put(b, a);
                    rmp.put(a, b);
                }
                else if (!mp.containsKey(b) || !rmp.containsKey(a)){
                    match = false;
                    break;
                }
                else if (mp.get(b) != a && rmp.get(a) != b) {
                    match = false;
                    break;
                }
            }
            if (match) {
                ret.add(word);
            }
        }
        return ret;
    }
}