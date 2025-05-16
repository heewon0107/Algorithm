import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // 배추흰지렁이 구입하기
        // 1. 지렁이는 인접한 배추로 이동 가능. 상하좌우
        // 2.

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine()); // 테스트케이스
        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken()); // 배추밭의 가로 길이
            int n = Integer.parseInt(st.nextToken()); // 배추밭의 세로 길이
            int k = Integer.parseInt(st.nextToken()); // 배추의 개수
            int result = 0;

            int[][] farm = new int[n][m]; // 배추 농장 초기화
            // 배추 심기
            for (int j = 0; j < k; j++) {
                StringTokenizer cabbage = new StringTokenizer(br.readLine());
                int positionM = Integer.parseInt(cabbage.nextToken());
                int positionN = Integer.parseInt(cabbage.nextToken());
                farm[positionN][positionM]++;
            }

            for (int r = 0; r < n; r++) {
                for (int c = 0; c < m; c++) {
                    if (farm[r][c] == 1) {
                        result++;
                        farm[r][c] = 0;
                        access(r, c, farm, n, m);
                    }
                }
            }
            System.out.println(result);
        }
    }
    private static void access(int row, int col, int[][] farm, int n, int m) {
        int[][] delta = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (int[] d : delta) {
            int nr = row + d[0];
            int nc = col + d[1];
            if (0 <= nr && nr < n && 0 <= nc && nc < m && farm[nr][nc] == 1) {
                farm[nr][nc] = 0;
                access(nr, nc, farm, n, m);
            }
        }
    }

}
