class Solution {
    public List<String> wordSubsets(String[] words1, String[] words2) {
        Map<Character, Integer> fin = new HashMap<>();
        for (String word: words2) {
            Map<Character, Integer> m = new HashMap<>();
            int i = 0;
            while (i < word.length()) {
                char c = word.charAt(i++);
                m.put(c, m.getOrDefault(c, 0) + 1);
            }
            for (char c: m.keySet()) {
                fin.put(c, Math.max(fin.getOrDefault(c, 0), m.get(c)));
            }
        }
        List<String> ret = new ArrayList<>();
        for (String word: words1) {
            Map<Character, Integer> m = new HashMap<>();
            int i = 0;
            while (i < word.length()) {
                char c = word.charAt(i++);
                m.put(c, m.getOrDefault(c, 0) + 1);
            }
            boolean universal = true;
            for (char c: fin.keySet()) {
                universal &= m.getOrDefault(c, 0) >= fin.get(c);
                if (!universal) {
                    break;
                }
            }
            if (universal) {
                ret.add(word);
            }
        }
        return ret;
    }
}