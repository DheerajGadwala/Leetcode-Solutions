class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        String[] morse = {".-","-...","-.-.","-..",
                          ".","..-.","--.","....",
                          "..",".---","-.-",".-..",
                          "--","-.","---",".--.",
                          "--.-",".-.","...","-",
                          "..-","...-",".--","-..-",
                          "-.--","--.."
                          };
        Set<String> all = new HashSet<>();
        for (String word: words) {
            StringBuilder str = new StringBuilder();
            for (int i = 0; i < word.length(); i++) {
                str.append(morse[word.charAt(i) - 'a']);
            }
            all.add(str.toString());
        }
        return all.size();
    }
}