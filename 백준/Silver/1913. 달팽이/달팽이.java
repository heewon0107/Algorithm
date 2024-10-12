import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        int X = Integer.parseInt(br.readLine()); // target
        int[][] snail = new int[N][N];
        int init_1 = N / 2;

        // 달팽이 위치
        snail[init_1][init_1] = 1;
        int r, c;
        r = init_1; c = init_1;

        // target 결과
        int a = init_1 + 1;
        int b = init_1 + 1;

        // 방향 설정
        int d = 0;
        int[][] delta = {{-1,0},{0,1},{1,0},{0,-1}};
        int num = 1;
        int move_cnt = 0;
        int rotate_cnt = 0;
        int limit = 1;  //

        // 달팽이 배열 채우기
        while (num++ < N*N){
            if (move_cnt == limit) { // 두 번 체크
                move_cnt = 0;    // 반복 초기화
                rotate_cnt++; // 회전수
                d = (d+1) % 4;
            }
            move_cnt++;
            // 두번 회전 시 갈수 있는 Limit++
            if (rotate_cnt == 2){
                limit++;
                rotate_cnt = 0;
            }
            r += delta[d][0];
            c += delta[d][1];
            snail[r][c] = num;
            if (snail[r][c] == X) {
                a = r + 1;
                b = c + 1;
            }

        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                sb.append(snail[i][j]).append(" ");
            }
            sb.append("\n");
        }
        sb.append(a).append(" ").append(b);
        System.out.println(sb.toString().trim());
    }
}
