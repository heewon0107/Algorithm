import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[][] board;
    static String result = "Hing";
    static int R, C;
    static int[][] delta = {{1,0}, {0,1}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        R = C = N-1;
        board = new int[N][N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        jelly(0, 0);
        System.out.println(result);
    }
    static void jelly(int r, int c) {
        if (r == R && c == C) {
            result = "HaruHaru";
            return;
        }
        int can_go = board[r][c];
        if (can_go == 0) {
            return;
        }
        for (int[] d : delta) {
            int nr = r + d[0] * can_go;
            int nc = c + d[1] * can_go;
            if (is_valid(nr,nc)){
                jelly(nr, nc);
            }
        }
    }
    static boolean is_valid(int nr, int nc) {
        return nr < N && nc < N;
    }
}
