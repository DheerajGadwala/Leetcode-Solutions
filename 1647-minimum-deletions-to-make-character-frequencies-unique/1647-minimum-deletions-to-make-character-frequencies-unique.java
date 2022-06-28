class Solution {
    public int minDeletions(String s) {
        Map<Character, Integer> f = new HashMap<>();
        for (char c: s.toCharArray()) {
            if (f.containsKey(c)) {
                f.put(c, f.get(c) + 1);
            }
            else {
                f.put(c, 1);
            }
        }
        int deletions = 0;
        Set<Integer> cnts = new HashSet<>();
        List<Character> chars = new ArrayList<>(f.keySet());
        int i = 0;
        while (i < chars.size()) {
            char c = chars.get(i);
            if (!cnts.contains(f.get(c))) {
                cnts.add(f.get(c));
                i++;
            }
            else if (f.get(c) == 0) {
                i++;
            }
            else {
                deletions++;
                f.put(c, f.get(c) - 1);
            }
        }
        return deletions;
    }
}