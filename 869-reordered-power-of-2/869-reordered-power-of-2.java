class Solution {
    public boolean reorderedPowerOf2(int n) {
        Set<String> s = new HashSet<>();
        s.add("1");
        int i = 1;
        while (i > 0) {
            StringBuilder sb = new StringBuilder();
            char[] k = (i+"").toCharArray();
            Arrays.sort(k);
            for (char c: k) {
                sb.append(c);
            }
            s.add(sb.toString());
            i <<= 1;
        }
        char[] k = (n+"").toCharArray();
        Arrays.sort(k);
        StringBuilder sb = new StringBuilder();
        for (char c: k) {
            sb.append(c);
        }
        return s.contains(sb.toString());
    }
}