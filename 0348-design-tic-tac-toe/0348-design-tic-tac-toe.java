class TicTacToe {

    int[][] mat;
    int n;
    
    public TicTacToe(int n) {
        mat = new int[n][n];
        this.n = n;
    }
    
    public int move(int row, int col, int player) {
        mat[row][col] = player;
        int i;
        for (i = 0; i < n; i++) {
            if (mat[row][i] != player) break;
            if (i == n - 1) return player;
        }
        for (i = 0; i < n; i++) {
            if (mat[i][col] != player) break;
            if (i == n - 1) return player;
        }
        for (i = 0; i < n; i++) {
            if (mat[i][i] != player) break;
            if (i == n - 1) return player;
        }
        for (i = 0; i < n; i++) {
            if (mat[n - i - 1][i] != player) break;
            if (i == n - 1) return player;
        }
        return 0;
    }
}

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe obj = new TicTacToe(n);
 * int param_1 = obj.move(row,col,player);
 */