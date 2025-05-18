import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int tc = 1; tc <= 10; tc++) {
            int N = Integer.parseInt(br.readLine());
            int[] tree = new int[N+1];
            int[] left = new int[N+1];
            int[] right = new int[N+1];
            String[] value = new String[N+1];

            for (int i = 1; i <= N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int cnt = st.countTokens();
                int node = Integer.parseInt(st.nextToken());
                tree[node] = node;
                value[node] = st.nextToken();

                if (cnt == 3) {
                    left[node] = Integer.parseInt(st.nextToken());
                } else if (cnt == 4) {
                    left[node] = Integer.parseInt(st.nextToken());
                    right[node] = Integer.parseInt(st.nextToken());
                }
            }

            // in order
            StringBuilder sb = new StringBuilder();
            Inorder(1, left, right, sb, value);
            System.out.println("#" + tc + " " + sb);
        }
    }
    private static void Inorder(int node, int[] left, int[] right, StringBuilder sb, String[] value) {
        if (node == 0) {
            return;
        }

        Inorder(left[node], left, right, sb, value);
        sb.append(value[node]);
        Inorder(right[node],left, right, sb, value);
    }
}
