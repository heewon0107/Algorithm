import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] r_chk = new int[N];
        int[] c_chk = new int[M];
        // 국룰 2차원 배열 만들기.
        char[][] place = new char[N][M];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                if (line.charAt(j) == 'X') {
                    r_chk[i] = 1;
                    c_chk[j] = 1;
                }
            }
        }
        int r_num = 0, c_num = 0;
        for (int r : r_chk) {
            if (r == 0) {
                r_num++;
            }
        }
        for (int c : c_chk) {
            if (c == 0) {
                c_num++;
            }
        }
        System.out.println(Math.max(r_num, c_num));

    }
}
