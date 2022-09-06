class Solution {
    
    class Pair implements Comparable<Pair>{
        int num, diff;
        
        public Pair(int num, int diff)
        {
            this.num = num;
            this.diff = diff;
        }
        
        @Override
        public int compareTo(Pair pair)
        {
            int res = Integer.compare(diff, pair.diff);
            if (res == 0) return Integer.compare(num, pair.num);
            else return res;
        }
    }
    
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        
        List<Integer> result = new ArrayList<>();
        if(arr == null || arr.length == 0) return result;
        
        Pair[] pairArray = new Pair[arr.length];
        
        for(int i =0;i<arr.length;i++)
        {
            pairArray[i] = new Pair(arr[i], Math.abs(arr[i] - x));
            
        }
        
        Arrays.sort(pairArray, new Comparator<Pair>() {
            @Override
            public int compare(Pair p1, Pair p2) {
                return p1.compareTo(p2);
            }
        });
        
       for(int i =0;i<k;i++)
       {
           result.add(pairArray[i].num);
       }
        
        Collections.sort(result);
        
        return result;
    }
}