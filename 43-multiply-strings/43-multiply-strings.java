class Solution {
    public String multiply(String num1, String num2) {
        
        int[] n1 = new int[num1.length()], n2 = new int[num2.length()];
        
        for (int i = 0; i < num1.length(); i++) {
            n1[num1.length() - 1 - i] = Integer.parseInt(num1.charAt(i)+"");
        }
        for (int i = 0; i < num2.length(); i++) {
            n2[num2.length() - 1 - i] = Integer.parseInt(num2.charAt(i)+"");
        }
        
        int[] res = new int[n1.length + n2.length + 1];
        
        int diff = 0;
        
        for (int i = 0; i < n1.length; i++) {
            for (int j = 0; j < n2.length; j++) {
                int al = res[diff + j];
                int bl = res[diff + j + 1];
                res[diff + j] = (al + n1[i] * n2[j]) % 10;
                res[diff + j + 1] = (int) (bl + (al + n1[i] * n2[j]) / 10);
            }
            diff++;
        }
        
        String ret = "";
        boolean flag = true;
        for (int i = res.length - 1; i > -1; i--) {
            if (res[i] == 0 && flag) {
                continue;
            }
            else {
                ret += res[i];
                flag = false;
            }
        }
        
        return ret.equals("") ? "0" : ret;
        
    }
}