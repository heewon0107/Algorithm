import java.io.*;
import java.util.StringTokenizer;

public class Solution {
    static int V,E,N1,N2, result;
    static int[] left,right;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            V = Integer.parseInt(st.nextToken());
            E = Integer.parseInt(st.nextToken());
            N1 = Integer.parseInt(st.nextToken());
            N2 = Integer.parseInt(st.nextToken());
            result = 0;
            left = new int[V+1]; right = new int[V+1];
            int[] parent = new int[V+1];
            StringTokenizer lst = new StringTokenizer(br.readLine());
            for (int i = 0; i < E; i++) {
                int s = Integer.parseInt(lst.nextToken());
                int e = Integer.parseInt(lst.nextToken());
                if (left[s] == 0) {
                    left[s] = e;
                } else {
                    int temp = left[s];
                    left[s] = Math.min(temp, e);
                    right[s] = Math.max(temp, e);
                }
                parent[e] = s;
            }

            int sameParent = N1;
            int node;
            while (parent[sameParent] != 0) {
                node = sameParent;
                sameParent = parent[sameParent];
                parent[node] = -1;
            }
            parent[sameParent] = -1;

            sameParent = N2;
            while (parent[sameParent] != -1) {
                sameParent = parent[sameParent];
            }
            
            tree(sameParent);
            StringBuilder sb = new StringBuilder();
            sb.append("#" + tc + " " + sameParent + " " + result);
            bw.write(sb.toString());
            bw.newLine();
        }
        bw.flush();
        bw.close();
        br.close();
    }
    private static void tree(int node) {
        if (node == 0) {
            return;
        }
        result++;
        tree(left[node]);
        tree(right[node]);
    }
}
