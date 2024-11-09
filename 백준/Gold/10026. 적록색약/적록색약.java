import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static int[][] delta = {{0,1},{0,-1},{1,0},{-1,0}};
    static int N;
    static char[][] picture;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        if (N == 1) {
            System.out.println("1 1");
            return;
        }
        picture = new char[N][N];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < N; j++) {
                picture[i][j] = line.charAt(j);
            }
        }

        // 일반인과 적록색약인 체크리스트
        boolean[][] ordinary_check = new boolean[N][N];
        boolean[][] redGreen_check = new boolean[N][N];
        int ordinaryCount = 0;
        int redGreenCount = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                // 해당 구역이 비었다.
                // 일반인용
                if (!ordinary_check[i][j]) {
                    ordinaryCount++;
                    // 델타 순회
                    dfsForOrdinary(i, j, picture[i][j], ordinary_check);
                }
                // 색록용
                if (!redGreen_check[i][j]) {
                    redGreenCount++;
                    dfsForRedGreen(i, j ,picture[i][j], redGreen_check);
                }

            }
        }
        System.out.println(ordinaryCount + " " + redGreenCount);
    }
    private static void dfsForRedGreen(int r, int c, char currentColor, boolean[][] check) {
        Queue<Integer[]> q = new LinkedList<>();
        q.add(new Integer[] {r, c});
        check[r][c] = true;

        while (!q.isEmpty()) {
            Integer[] del = q.poll();
            int x = del[0], y = del[1];

            for (int[] d : delta) {
                int nr = x + d[0];
                int nc = y + d[1];

                if (0 <= nr && nr < N && 0 <= nc && nc < N && !check[nr][nc]) {
                    if (picture[nr][nc] == currentColor) {
                        q.add(new Integer[] {nr,nc});
                        check[nr][nc] = true;
                    } else if (currentColor == 'R' || currentColor == 'G') {
                        if (picture[nr][nc] == 'R' || picture[nr][nc] == 'G') {
                            check[nr][nc] = true;
                            q.add(new Integer[]{nr, nc});
                        }
                    }
                }
            }
        }
    }
    private static void dfsForOrdinary(int r, int c, char currentColor, boolean[][] check) {
        Queue<Integer[]> q = new LinkedList<>();
        q.add(new Integer[] {r, c});
        check[r][c] = true;

        while (!q.isEmpty()) {
            Integer[] del = q.poll();
            int x = del[0], y = del[1];

            for (int[] d : delta) {
                int nr = x + d[0];
                int nc = y + d[1];

                if (0 <= nr && nr < N && 0 <= nc && nc < N && !check[nr][nc]) {
                    if (picture[nr][nc] == currentColor) {
                        q.add(new Integer[] {nr,nc});
                        check[nr][nc] = true;
                    }
                }
            }
        }
    }
}