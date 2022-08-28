class Solution {
    
    int maxPos;
    String tiles;
    boolean[] visited;
    Set<String> perms;
    
    public int numTilePossibilities(String tiles) {
        this.tiles = tiles;
        visited = new boolean[tiles.length()];
        perms = new HashSet<>();
        for (int i = 1; i < tiles.length() + 1; i++) {
            maxPos = i;
            res(0, "");
        }
        return perms.size();
    }
    
    private void res(int pos, String acc) {
        if (pos == maxPos) {
            perms.add(acc);
        }
        else {
            for (int i = 0; i < tiles.length(); i++) {
                if (!visited[i]) {
                    visited[i] = true;
                    res(pos + 1, acc + tiles.charAt(i));
                    visited[i] = false;
                }
            }
        }
    }
}