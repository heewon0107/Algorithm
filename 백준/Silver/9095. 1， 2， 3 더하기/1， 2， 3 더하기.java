import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            int n = Integer.parseInt(br.readLine());
            int[] arr = new int[n+1];
            for (int j = 1; j < n+1; j++) {
                if (j==1) {
                    arr[j] = 1;
                }
                else if (j==2) {
                    arr[j] = 2;
                }
                else if (j==3) {
                    arr[j] = 4;
                } else {
                    arr[j] = arr[j-3] + arr[j-2] + arr[j-1];
                }
            }
            System.out.println(arr[n]);

        }
    }
}
