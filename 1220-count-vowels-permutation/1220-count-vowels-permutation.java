class Solution {
    int n;
    HashMap<Character, String> map;
    HashMap<Integer, HashMap<Character,Long>> cache;
    long mod = (long) Math.pow(10,9)+7;
    
    public int countVowelPermutation(int n) {
        this.n = n;
        map = new HashMap<>();
        cache = new HashMap<>();
        
        
        map.put('a',"e");
        map.put('e',"ai");
        map.put('i',"aeou");
        map.put('o', "iu");
        map.put('u',"a");
        
        long ret = 0;
        
        for(Character c : map.keySet()){
            ret= (ret + dfs(1,c)) % mod;
        }
     return (int)ret;   
    }
    
    
    public long dfs(int pos, char curr){
        if(pos==n) return 1;
        
        if(cache.containsKey(pos) && cache.get(pos).containsKey(curr)){
            return cache.get(pos).get(curr);
        }
        else if(! cache.containsKey(pos) ){
            cache.put(pos, new HashMap<>());
        }
        
        long ret = 0;
        for(Character a : map.get(curr).toCharArray()){
            ret = (ret + dfs(pos+1, a)) % mod;
        }
        cache.get(pos).put(curr, ret);
        return ret;
    }
}