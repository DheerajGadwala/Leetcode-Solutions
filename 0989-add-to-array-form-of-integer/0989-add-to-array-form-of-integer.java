class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
        List<Integer> ret = new LinkedList<>();
        int carry = 0, i = num.length - 1;
        while (i > -1 || k > 0 || carry > 0) {
            int val = k % 10 + carry + (i > -1 ? num[i] : 0);
            ret.add(val % 10);
            carry = val / 10;
            i--;
            k /= 10;
        }
        if (carry != 0) ret.add(0, carry);
        int t = 0, j = ret.size() - 1;
        while (t < j) {
            ret.set(t, ret.get(t) + ret.get(j));
            ret.set(j, ret.get(t) - ret.get(j));
            ret.set(t, ret.get(t) - ret.get(j));
            t++;
            j--;
        }
        return ret;
    }
}