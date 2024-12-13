import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] numbers = new int[201]; // -100 ~ 100 까지 수 담을 공간
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int number = Integer.parseInt(st.nextToken());
            if (number < 0) {
                numbers[-number + 100]++;
            }
            else {
                numbers[number]++;
            }
        }
        int targetNumber = Integer.parseInt(br.readLine());
        if (targetNumber < 0) {
            targetNumber = 100 - targetNumber;
        }
        System.out.println(numbers[targetNumber]);
        br.close();

    }
}
