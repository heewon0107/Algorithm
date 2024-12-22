import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] buckets = new int[N];

        for (int i = 0; i < M; i++) {
            StringTokenizer insertMenu = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(insertMenu.nextToken()) - 1;
            int end = Integer.parseInt(insertMenu.nextToken());
            int ballNumber = Integer.parseInt(insertMenu.nextToken());

            for (int j = start; j < end; j++) {
                buckets[j] = ballNumber;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int bucket : buckets) {
            sb.append(bucket).append(" ");
        }
        System.out.println(sb.toString().trim());



    }
}
