import java.io.*;
import java.util.*;

public class Solution {
    static boolean[] connect;
    static List<List<Integer>> adjList = new ArrayList<>(); // 인접 리스트 생성

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc < T+1; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N,M;
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            connect = new boolean[N+1]; // 연결 되어 있는
            adjList.clear();
            for (int i = 0; i <= N; i++) {
                adjList.add(new ArrayList<>());
            }

            for (int i = 0; i < M; i++) {
                StringTokenizer lst = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(lst.nextToken());
                int v = Integer.parseInt(lst.nextToken());

                adjList.get(u).add(v);
                adjList.get(v).add(u);
            }
            int result = 0;
            for (int i = 1; i < N+1; i++) {
                if (connect[i]) {
                    continue;
                }
                Rotate(i);
                result++;

            }
            System.out.println("#" + tc + " " + result);
        }
    }
    private static void Rotate(int man) {
        connect[man] = true;
        if (adjList.get(man).isEmpty()) {
            return;
        }
//        Stack<Integer> stack = new Stack<>();
//        stack.push(man);
        

//        while (!stack.isEmpty()) {
//            int node = stack.pop();

            for (Integer neighbor : adjList.get(man)) {
                if (connect[neighbor]) {
                    continue;
                }
                Rotate(neighbor);
//                stack.push(neighbor);
            }
//        }
    }
}
