import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] time = new int[N];

        for (int i = 0; i < time.length; i++) {
            time[i] = Integer.parseInt(st.nextToken());
        }
        for (int i = 0; i < N-1; i++) {
            for (int j = 0; j < N-1-i; j++) {
                if (time[j] > time[j+1]) {
                    int temp = time[j];
                    time[j] = time[j + 1];
                    time[j + 1] = temp;
                }
            }
        }
        int result = 0;
        for (int i = 0; i < N; i++) {
            if (i == 0) {
                result += time[0];
                continue;
            }
            time[i] += time[i-1];
            result += time[i];
        }
        System.out.println(result);
    }
}
