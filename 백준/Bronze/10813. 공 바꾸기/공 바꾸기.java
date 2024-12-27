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
        int[] balls = new int[N];

        // 공 번호 입력 1 ~ N
        for (int i = 0; i < N; i++) {
            balls[i] = i+1;
        }
        // 공 교환 시작 ~M
        for (int i = 0; i < M; i++) {
            StringTokenizer exchange = new StringTokenizer(br.readLine());
            int firstBallNum = Integer.parseInt(exchange.nextToken()) - 1;
            int secondBallNum = Integer.parseInt(exchange.nextToken()) - 1;
            if (firstBallNum == secondBallNum) {
                continue;
            }
            int firstBall = balls[firstBallNum];
            int secondBall = balls[secondBallNum];

            balls[firstBallNum] = secondBall;
            balls[secondBallNum] = firstBall;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N - 1; i++) {
            sb.append(balls[i]).append(" ");
        }
        sb.append(balls[N-1]);

        System.out.println(sb.toString().trim());
        br.close();
    }
}
