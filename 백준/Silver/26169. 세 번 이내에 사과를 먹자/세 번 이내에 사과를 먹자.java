import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int result = 0;
    static int[][] board = new int[5][5];
    static int[][] delta = {{-1,0}, {1,0}, {0,-1}, {0, 1}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 5; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        StringTokenizer st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        board[r][c] = -1;
        Apple(r, c, 0, 0);
        System.out.println(result);
    }
    static void Apple(int r, int c, int eat, int move) {

        if (result == 1) {
            return;
        }
        if (eat == 2) {
            result = 1;
            return;
        }
        if (move == 3) {
            return;
        }
        for (int[] d : delta) {
            int nr = r + d[0];
            int nc = c + d[1];
            if (is_valid(nr, nc) && board[nr][nc] != -1) {
                int origin = board[nr][nc];
                if (board[nr][nc] == 1){
                    board[nr][nc] = -1;
                    Apple(nr, nc, eat + 1, move + 1);
                    board[nr][nc] = 1;
                    continue;
                }
                board[nr][nc] = -1;
                Apple(nr, nc, eat, move + 1);
                board[nr][nc] = 0;
            }
        }
    }
    static boolean is_valid(int nr, int nc) {
        return 0 <= nr && nr < 5 && 0 <= nc && nc < 5;
    }
}
