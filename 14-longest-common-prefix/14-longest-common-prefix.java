class Solution {
    public String longestCommonPrefix(String[] strs) {
        int i = -1;
        boolean flag = true;
        while (flag) {
            i++;
            char a;
            if (i < strs[0].length())
                a = strs[0].charAt(i);
            else
                break;
            for (int j = 1; j < strs.length; j++) {
                flag &= i < strs[j].length() && strs[j].charAt(i) == a;
            }
        }
        return strs[0].substring(0, i);
    }
}