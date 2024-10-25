import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        long M = Long.parseLong(input[1]);
        long[] arr = new long[N];
        
        String[] arrInput = br.readLine().split(" ");
        for (int i = 0; i < N; i++) {
            arr[i] = Long.parseLong(arrInput[i]);
        }

        long result = 0;
        long currentSum = 0;
        Map<Long, Long> countMap = new HashMap<>();
        countMap.put(0L, 1L); // 0 나머지는 초기값으로 1

        for (int i = 0; i < N; i++) {
            currentSum += arr[i];
            long mod = currentSum % M;

            // mod가 음수일 경우 처리
            if (mod < 0) {
                mod += M;
            }

            // 현재 나머지와 같은 나머지를 가진 경우의 수를 더함
            result += countMap.getOrDefault(mod, 0L);

            // 현재 나머지를 카운트
            countMap.put(mod, countMap.getOrDefault(mod, 0L) + 1);
        }

        System.out.println(result);
    }
}
