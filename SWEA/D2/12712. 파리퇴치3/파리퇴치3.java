
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine()); // 테스트케이스
        int[][] plusDelta = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        int[][] xDelta = {{-1, -1}, {1, 1}, {1, -1}, {-1, 1}};
        for (int i = 1; i <= testCase; i++) {
            int N, range;
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken()); // N x N 영역
            range = Integer.parseInt(st.nextToken()); // 스프레이의 세기
            String[][] flyArray = new String[N][N];
            for (int j = 0; j < N; j++) {
                String line = br.readLine();
                flyArray[j] = line.split(" ");
            }
            // 출력할 최대의 파리잡기
            int maxKill = 0;
            for (int row = 0; row < N; row++) {
                for (int col = 0; col < N; col++) {
                    // 현재 좌표의 파리 수
                    int plusKill = Integer.parseInt(flyArray[row][col]);
                    int xKill = Integer.parseInt(flyArray[row][col]);
                    // 범위 탐색시작
                    for (int l = 1; l < range; l++) {
                        // 플러스 범위 탐색
                        for (int[] d : plusDelta) {
                            int nextRow = row + d[0] * l;
                            int nextCol = col + d[1] * l;
                            if (0 <= nextRow && nextRow < N && 0 <= nextCol && nextCol < N) {
                                plusKill += Integer.parseInt(flyArray[nextRow][nextCol]);
                            }
                        }

                        for (int[] d : xDelta) {
                            int nextRow = row + d[0] * l;
                            int nextCol = col + d[1] * l;
                            if (0 <= nextRow && nextRow < N && 0 <= nextCol && nextCol < N) {
                                xKill += Integer.parseInt(flyArray[nextRow][nextCol]);
                            }
                        }

                    }
                    // 범위 탐색 끝 최대 킬 수 비교
                    int relateKill = Math.max(plusKill, xKill);
                    maxKill = Math.max(relateKill, maxKill);
                }
            }
            System.out.println("#" + i + " " + maxKill);


        }

    }
}
