class Solution {
    
    Map<Integer, Map<Map<Character, Integer>, Integer>> cache;
    Map<Character, Integer> score;
    String[] words;
    
    public int maxScoreWords(String[] words, char[] letters, int[] score) {
        Map<Character, Integer> c = new HashMap<>(), s = new HashMap<>();
        for (int i = 'a'; i <= 'z'; i++) {
            c.put((char) i, 0);
        }
        for (char t: letters) {
            c.put(t, c.get(t) + 1);
        }
        for (int i = 0; i < score.length; i++) {
            s.put((char) (i + 97), score[i]);
        }
        this.score = s;
        this.words = words;
        this.cache = new HashMap<>();
        return res(0, c);
    }
    
    public int res(int pos, Map<Character, Integer> count) {
        if (!cache.containsKey(pos)) {
            cache.put(pos, new HashMap<>());
        }
        if (pos == words.length) {
            return 0;
        }
        else {
            String word = words[pos];
            Map<Character, Integer> letterCount = new HashMap<>();
            for (char t: word.toCharArray()) {
                if (!letterCount.containsKey(t)) {
                    letterCount.put(t, 1);
                }
                else {
                    letterCount.put(t, letterCount.get(t) + 1);
                }
            }
            Map<Character, Integer> copy = new HashMap<>(count);
            int s = 0;
            boolean isValid = true;
            for (char t: letterCount.keySet()) {
                copy.put(t, copy.get(t) - letterCount.get(t));
                s += letterCount.get(t) * score.get(t);
                if (copy.get(t) < 0) {
                    isValid = false;
                    break;
                }
            }
            if (isValid) {
                cache.get(pos).put(copy, Math.max(s + res(pos + 1, copy), res(pos + 1, count)));
                return cache.get(pos).get(copy);
            }
            else {
                cache.get(pos).put(count, res(pos + 1, count));
                return cache.get(pos).get(count);
            }
        }
    }
    
}