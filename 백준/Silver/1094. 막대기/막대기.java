import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static int[] sticks = {1, 2, 4, 8, 16, 32, 64};
    private static int target;
    private static int result = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        target = Integer.parseInt(br.readLine());
        
        for (int stick : sticks) {
            if (stick == target) {
                result = 1;
                break;
            }
        }
        if (result == 1) {
            System.out.println(result);
        } else {
            for (int i = 0; i < sticks.length; i++) {

                stick(i + 1, 1, sticks[i]); // 스틱 붙이고 다음 스틱 보러감.
            }
            System.out.println(result);
        }


        br.close();
    }

    public static void stick(int idx, int cnt, int stick) {
        // 기저조건.
        if (idx == sticks.length) { // idx가 범위 밖
            return;
        }
        if (cnt > result) { // cnt 가 더 클 때
            return;
        } else if (stick > target) { // 붙인 막대기가 더 클 때.
            return;
        }
        if (stick == target) { // 타겟 막대기 길이에 도달.
            if (result > cnt) { // 붙인 횟수 비교.
                result = cnt;
            }
            return;
        }

        for (int i = idx; i < sticks.length; i++) {
            stick(i + 1, cnt + 1, stick + sticks[idx]); // 지금 스틱을 붙이고 재귀
            stick(i + 1, cnt, stick);                    // 안붙이고 재귀.

        }
    }
}
