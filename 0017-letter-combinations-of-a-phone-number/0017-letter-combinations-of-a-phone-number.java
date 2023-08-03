class Solution {
    
    List<String> li;
    HashMap<Character, String> mapping;
    String digits;
    
    
    public HashMap<Character, String> createMapping() {
        HashMap<Character, String> mapping = new HashMap();
        mapping.put('2', "abc");
        mapping.put('3', "def");
        mapping.put('4', "ghi");
        mapping.put('5', "jkl");
        mapping.put('6', "mno");
        mapping.put('7', "pqrs");
        mapping.put('8', "tuv");
        mapping.put('9', "wxyz");
        return mapping;
    }
    
    public List<String> letterCombinations(String digits) {
        mapping = createMapping();
        this.digits = digits;
        li = new ArrayList<>();
        
        if (digits.length() == 0) {
            return li;
        }
        
        generate("");
        
        return li;
    }
    
    void generate(String out) {
        if (out.length() == digits.length()) {
            li.add(out);
        }
        else {
            int i = out.length();
            String s = mapping.get(digits.charAt(i));

            for(char c: s.toCharArray()) {
                generate(out + c);
            }
        }
        


    }
}