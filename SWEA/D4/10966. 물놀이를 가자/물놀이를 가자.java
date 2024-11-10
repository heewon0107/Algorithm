import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
    static int[][] delta = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N, M;
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            char[][] land = new char[N][M];
            int[][] visited = new int[N][M];
            Queue<int[]> q = new LinkedList<>();

            for (int i = 0; i < N; i++) {
                String line = br.readLine();
                for (int j = 0; j < M; j++) {
                    land[i][j] = line.charAt(j);
                    if (land[i][j] == 'W') {
                        q.add(new int[] {i,j});
                        visited[i][j] = -1;
                    }
                }
            }
            //물 우선 탐색
            int result = 0;
            int cnt = 1;
            while (!q.isEmpty()) {
                int size = q.size();

                for (int i = 0; i < size; i++) {
                    int [] go = q.poll();
                    int r = go[0];
                    int c = go[1];
                    for (int[] del : delta) {
                        int nr = r + del[0];
                        int nc = c + del[1];
                        // 범위 체크
                        if (0 <= nr && nr < N && 0 <= nc && nc < M && visited[nr][nc] != -1) {
                            // 첫 방문
                            if (visited[nr][nc] == 0) {
                                visited[nr][nc] = cnt;
                                q.add(new int[] {nr,nc});
                            }
                            // 두 번째 방문
                            else if (visited[nr][nc] > 0) {
                                if (visited[nr][nc] > cnt) {
                                    visited[nr][nc] = cnt;
                                    q.add(new int[] {nr,nc});
                                }

                            }
                        }
                    }
                }
                cnt++;
            }
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (visited[i][j] > 0) {
                        result += visited[i][j];
                    }
                }
            }
            System.out.println("#" + tc + " " + result);
        }
    }
}
