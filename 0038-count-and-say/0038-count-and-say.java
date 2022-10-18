class Solution {
    
    HashMap<Integer, String> mem = new HashMap<Integer, String>();
    
    String say(String s){
        char prev = 'a';
        String const_ = "";
        int cnt = 0;
        for(char k: s.toCharArray()){
            if(k!=prev){
                if(prev!='a'){
                    const_+=Integer.toString(cnt)+prev;
                }
                prev=k;
                cnt=1;
            }
            else{
                cnt++;
            }
        }
        const_+=Integer.toString(cnt)+prev;
        return const_;
    }
    
    public String countAndSay(int n) {
        if(this.mem.containsKey(n)){
            return this.mem.get(n);
        }
        else{
            this.mem.put(1, "1");
            for(int i = 2; i<31; i++){
                this.mem.put(i, this.say(this.mem.get(i-1)));
            }
        }
        return this.mem.get(n);
    }
}