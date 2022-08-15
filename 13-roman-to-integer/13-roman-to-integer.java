class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> vals = new HashMap<Character, Integer>();
        vals.put('I', 1);
        vals.put('V', 5);
        vals.put('X', 10);
        vals.put('L', 50);
        vals.put('C', 100);
        vals.put('D', 500);
        vals.put('M', 1000);
        int prev = 0;
        int sum = 0;
        for(int i = s.length()-1; i>=0; i--){
            if (vals.get(s.charAt(i))>=prev){
                sum+=vals.get(s.charAt(i));
                prev=vals.get(s.charAt(i));
            }
            else{
                sum-=vals.get(s.charAt(i));
            }
        }
        return sum;
    }
}