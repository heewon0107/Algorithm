#include <string>
#include <vector>

using namespace std;


int solution(vector<vector<string>> board, int h, int w) {
    
    
    int answer = 0;
    int N = board.size();
    int M = board[0].size();
    
    auto is_valid = [&](int r, int c) {
        return 0 <= r && r < N && 0 <= c && c < M;
    };
    
    int dr[4] = {-1, 1, 0, 0};
    int dc[4] = {0, 0, -1, 1};
    
    string color = board[h][w];
    
    for (int d = 0; d < 4; d++) {
        int nr = h + dr[d];
        int nc = w + dc[d];
        
        if (is_valid(nr, nc) && board[nr][nc] == color) {
            answer++;
        }
    }
    return answer;
}