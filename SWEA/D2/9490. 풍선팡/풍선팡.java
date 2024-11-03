import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());
        for (int tc = 1; tc < testCase+1; tc++) {

            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int[][] balloon = new int[N][M];
            for (int i = 0; i < N; i++) {
                StringTokenizer line = new StringTokenizer(br.readLine());
                for (int j = 0; j < M; j++) {
                    balloon[i][j] = Integer.parseInt(line.nextToken());
                }

            }
            int result = 0;
            int[][] delta = {{-1,0}, {1,0}, {0,-1}, {0,1}};
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    int sum = balloon[i][j];
                    for (int[] del : delta) {
                        for (int k = 1; k < balloon[i][j]+1; k++) {
                            int ni = i + del[0] * k;
                            int nj = j + del[1] * k;
                            if (0 <= ni && ni < N && 0 <= nj && nj < M) {
                                sum += balloon[ni][nj];
                            }
                        }
                    }result = Math.max(result, sum);
                }
            }
            System.out.println("#"+tc+" "+ result);

        }
    }
}
