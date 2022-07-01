class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        Arrays.sort(boxTypes, (a, b) -> -Integer.compare(a[1], b[1]));
        int ans = 0, i = 0;
        while (truckSize != 0 && i < boxTypes.length) {
            if (boxTypes[i][0] <= truckSize) {
                truckSize -= boxTypes[i][0];
                ans += boxTypes[i][0] * boxTypes[i][1];
            }
            else {
                ans += truckSize * boxTypes[i][1];
                truckSize = 0;
            }
            i++;
        }
        return ans;
    }
}