class Solution {
    public String[] reorderLogFiles(String[] logs) {
        
        Arrays.sort(logs, new Comparator<String>() {
            @Override
            public int compare(String a, String b) {
                String[] aa = a.split(" ");
                StringBuilder arem = new StringBuilder();
                String[] ba = b.split(" ");
                StringBuilder brem = new StringBuilder();
                for (int i = 1; i < aa.length; i++) arem.append(aa[i]+" ");
                for (int i = 1; i < ba.length; i++) brem.append(ba[i]+" ");
                boolean adig = aa[1].charAt(0) - 48 >= 0 && aa[1].charAt(0) - 48 <= 9, bdig = ba[1].charAt(0) - 48 >= 0 && ba[1].charAt(0) - 48 <= 9;
                if (adig && bdig) {
                    return 0;
                }
                else if (!adig && !bdig) {
                    if (arem.toString().compareTo(brem.toString()) == 0) return aa[0].compareTo(ba[0]);
                    else return arem.toString().compareTo(brem.toString());
                }
                else if (adig) {
                    return 1;
                }
                else {
                    return -1;
                }
            }
        });
        
        return logs;
        
    }
}