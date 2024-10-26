import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N+1];

        if (N == 3) {
            System.out.println(1);
            return;
        } else if (N == 4) {
            System.out.println(-1);
            return;
        } else if (N == 5) {
            System.out.println(1);
            return;
        }
        for (int i = 0; i < N+1; i++) {
            arr[i] = -1;
        }

        arr[3] = 1;
        arr[5] = 1;

        for (int i = 6; i < N+1; i++) {
            if (arr[i-3] != -1) {
                arr[i] = arr[i-3] + 1;
            } else if (arr[i-5] != -1) {
                arr[i] = arr[i-5] + 1;
            }
            if (arr[i-3] != -1 && arr[i-5] != -1) {
                arr[i] = Math.min(arr[i-3], arr[i-5]) + 1;
            }

        }
        System.out.println(arr[N]);

    }
}