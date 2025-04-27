import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();

        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n, m;
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());

            sb.append("#" + tc + " " + binary(n, m) + "\n");
        }
        System.out.println(sb.toString().trim());

    }

    public static String binary(int n, int m) {
        int mask = (1 << n) - 1;
        if ((m & mask) == mask)
            return "ON";
         else return "OFF";
    }
}