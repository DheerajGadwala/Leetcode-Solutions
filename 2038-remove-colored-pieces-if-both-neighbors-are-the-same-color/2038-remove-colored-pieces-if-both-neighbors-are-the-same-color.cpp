class Solution {
public:
    bool winnerOfGame(string colors) {
        int n = colors.size();
        int a = 0, b = 0;
        for (int i = 2; i < n; i++) {
            if (colors[i] == colors[i-1] && colors[i] == colors[i-2]) {
                if (colors[i] == 'A') {
                    a++;
                }
                else {
                    b++;
                }
            }
        }
        return a > b;
    }
};