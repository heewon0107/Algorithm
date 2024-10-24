import java.util.Scanner;

public class Main {
    static int N;
    static int[][] board;
    static boolean[] visited;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();

        if (N == 1) {
            System.out.println(1);
            return;
        }else if (N == 2 || N == 3) {
            System.out.println(0);
            return;
        }
        board = new int[N][N];
        visited = new boolean[N];

        for (int i = 0; i < N; i++) {
            board[0][i] = 1;
            visited[i] = true;
            queen(1);
            board[0][i] = 0;
            visited[i] = false;
        }
        sc.close();
        System.out.println(result);

    }
    static int result = 0;
    static void queen(int row) {
        if (row == N) {
            result++;
            return;
        }

        // 위에 있음 안돼 j_chk
        for (int j = 0; j < N; j++) {
            if (!visited[j]) {// 위 쪽에 퀸이 없다.
                boolean can_go = true; // 대각 탐색 가능하다.

                int nr = row - 1;
                int nc_left = j - 1;
                // 좌상 탐색
                while (0 <= nr && 0 <= nc_left) {
                    // if문을 만나지 않으면 갈 수 있음.
                    if (board[nr][nc_left] == 1) {
                        can_go = false;
                    }
                    nr--;
                    nc_left--;
                }
                nr = row - 1;
                int nc_right = j + 1;
                // 우상 탐색
                while (0 <= nr && nc_right < N) {
                    if (board[nr][nc_right] == 1) {
                        can_go = false;
                    }
                    nr--;
                    nc_right++;
                }
                if (can_go) {
                    board[row][j] = 1;
                    visited[j] = true;
                    queen(row + 1);
                    board[row][j] = 0;
                    visited[j] = false;
                }
            }
        }

    }
}
