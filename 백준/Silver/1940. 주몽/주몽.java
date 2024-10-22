import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        int[] used = new int[n]; // 사용 흔적.
        int[] staff = new int[n]; // 재료 목록
        int result = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            staff[i] = Integer.parseInt(st.nextToken());
        }
        for (int i = 0; i < n-1; i++) {
            //재료 사용시 continue
            if (used[i] != 0) {
                continue;
            }
            for (int j = i+1; j < n; j++) {
                if (used[j] != 0) {
                    continue;
                }
                if (staff[i] + staff[j] == m) {
                    used[i] = 1;
                    used[j] = 1;
                    result++;
                }
            }
        }
        System.out.println(result);
    }
}
