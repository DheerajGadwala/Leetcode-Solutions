class Solution {
    public String reorganizeString(String s) {
        Map<Character, Integer> cnt = new HashMap<>();
        List<Character> chars = new ArrayList<>();
        int max = 0;
        for (char c: s.toCharArray()) {
            cnt.put(c, cnt.getOrDefault(c, 0) + 1);
            max = Math.max(max, cnt.get(c));
            chars.add(c);
        }
        Collections.sort(chars, new Comparator<Character>() {
            @Override
            public int compare(Character a, Character b) {
                int cmp = -Integer.compare(cnt.get(a), cnt.get(b));
                if (cmp == 0) return Character.compare(a, b);
                return -Integer.compare(cnt.get(a), cnt.get(b));
            }
        });
        List<StringBuilder> l = new ArrayList<>();
        for (int i = 0; i < max; i++) {
            l.add(new StringBuilder());
        }
        for (int i = 0; i < chars.size(); i++) {
            l.get(i%max).append(chars.get(i));
        }
        StringBuilder ret = new StringBuilder();
        for (StringBuilder b: l) {
            if (ret.length() > 0 && ret.charAt(ret.length() - 1) == b.charAt(0)) return "";
            ret.append(b);
        }
        return ret.toString();
    }
}