import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine()); // 1 <= N <= 1,000,000 : 시험장의 개수
        StringTokenizer line = new StringTokenizer(br.readLine());

        // 시험장 배열 만들기
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(line.nextToken());
        }
        int B, C;
        StringTokenizer st = new StringTokenizer(br.readLine());
        B = Integer.parseInt(st.nextToken()); // 총감독관이 한 시험장에서 감시할 수 있는 응시자의 수
        C = Integer.parseInt(st.nextToken()); // 부감독관이 한 시험장에서 감시할 수 있는 응시자의 수
        // 각 시험장에 총감독관은 오직 1명, 부감독관은 여려명 있어도 된다.
        // 총감독관은 무조건 있어야 되나?
        // 그렇다면 모든 시험장 remainNum = A - B
        // remainNum % C == 0 일 떄와 아닐 때
        long result = 0;
        for (int remainNum : arr) {
            remainNum -= B;
            result++;
            if (remainNum <= 0) {
                continue;
            }
            if (remainNum < C) {
                result++;
                continue;
            }
            if (remainNum % C == 0) {
                result += remainNum / C;
            } else {
                result += remainNum / C + 1;
            }
        }
        System.out.println(result);
        br.close();

    }
}
