import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] buckets = new int[n];
        for (int i = 0; i < n; i++) {
            buckets[i] = i + 1;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;

            int temp = buckets[a];
            buckets[a] = buckets[b];
            buckets[b] = temp;
        }

        StringBuilder sb = new StringBuilder();
        for (int bucket : buckets) {
            sb.append(bucket).append(" ");
        }
        System.out.println(sb.toString());
    }
}
