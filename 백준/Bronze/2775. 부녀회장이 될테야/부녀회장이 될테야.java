import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < T; tc++) {
            int k, n;
            k = Integer.parseInt(br.readLine()); // 층
            n = Integer.parseInt(br.readLine()); // 호

            int[][] apart = new int[k + 1][n];
            // 0층 부터 k-1층까지 1호 부터 n호까지 역순으로 저장.
            for (int i = 0; i < k + 1; i++) { // i 층
                for (int j = 0; j < n; j++) { // j 호
                    if (i == 0) { // 0층 j + 1호 사람은 j + 1명 거주
                        apart[i][j] = j + 1; // 1호부터 1명씩 추가.
                    } else { // 아랫층의 사람들 더해주기
                        for (int l = 0; l < j + 1; l++) {
                            apart[i][j] += apart[i - 1][l];
                        }
                    }

                }
            }

            System.out.println(apart[k][n - 1]);

        }

        br.close();
    }

}
