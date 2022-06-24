class Solution {
    
    public boolean isPossible(int[] target) {
        if (target.length == 1) {
            return target[0] == 1;
        }
        PriorityQueue<Integer> q = new PriorityQueue<>((a, b) -> -Integer.compare(target[a], target[b]));
        int sum = 0;
        for (int i = 0; i < target.length; i++) {
            sum+=target[i];
            q.add(i);
        }
        while (sum > target.length) {
            int maxPos=q.poll();
            int temp = target[maxPos];
            if (2 * target[maxPos] < sum) {
                return false;
            }
            target[maxPos] = sum-target[maxPos] == 1 ? 1 : target[maxPos] % (sum - target[maxPos]);
            sum = sum - temp + target[maxPos];
            if (target[maxPos] < 1) {
                return false;
            }
            q.add(maxPos);
            for (int i = 0; i < target.length; i++) {
                System.out.print(target[i] + " ");
            }
            System.out.println();
        }
        return sum == target.length;
    }
}