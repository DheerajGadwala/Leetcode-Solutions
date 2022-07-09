class Solution {
    
    public int maxResult(int[] nums, int k) {
        
        PriorityQueue<Integer[]> q = new PriorityQueue<>(new Comparator<Integer[]>(){
            @Override
            public int compare(Integer[] o1, Integer[] o2) {
                if (o1[0] == o2[0]) {
                    return -Integer.compare(o1[1], o2[1]);
                }
                else {
                    return -Integer.compare(o1[0], o2[0]);
                }
            }
        });
        
        q.add(new Integer[] {nums[0], 0});
        
        for (int i = 1; i < nums.length; i++) {
            while (i - q.peek()[1] > k) {
                q.poll();
            }
            if (i == nums.length - 1) {
                return q.peek()[0] + nums[i];
            }
            else {
                q.add(new Integer[] {q.peek()[0] + nums[i], i});   
            }
        }
        return nums[0];
    }
    
    
    
}