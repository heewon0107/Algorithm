import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine()); // 테스트케이스
        for (int tc = 1; tc <= T; tc++) {

            StringTokenizer st = new StringTokenizer(br.readLine());
            int V = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());
            int num1 = Integer.parseInt(st.nextToken());
            int num2 = Integer.parseInt(st.nextToken());
            int[] tree = new int[V + 1];
            int[] left = new int[V + 1];
            int[] right = new int[V + 1];
            int[] parents = new int[V + 1];

            // 트리 채우기
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < E; i++) {
                int parent = Integer.parseInt(st.nextToken());
                int child = Integer.parseInt(st.nextToken());
                parents[child] = parent;

                // 왼쪽 자식 있으면 오른쪽에 넣기.
                if (left[parent] != 0) {
                    right[parent] = child;
                } else {
                    left[parent] = child;
                }
            }

            int ancestor = findAncestor(parents, num1, num2);
            int treeSize = getSubTree(left, right, ancestor);

            sb.append("#" + tc + " " + ancestor + " " + treeSize + "\n");
        }
        System.out.println(sb);

    }
    
    // 깊이 찾기 함수
    private static int getDepth(int[] parents, int node) {
        int depth = 0;
        while (node != 0) {
            node = parents[node];
            depth++;
        }
        return depth;
    }
    // 공통 조상 찾기 함수
    private static int findAncestor(int[] parents, int num1, int num2) {
        int leftD = getDepth(parents, num1);
        int rightD = getDepth(parents, num2);
        
        while (leftD > rightD) {
            leftD--;
            num1 = parents[num1];
        }
        
        while (rightD > leftD) {
            rightD--;
            num2 = parents[num2];
        }
        
        while (num1 != num2) {
            num1 = parents[num1];
            num2 = parents[num2];
        }
        return num1;
    }

    // 서브트리 개수 함수
    private static int getSubTree(int[] left, int[] right, int node) {
        if (node == 0) return 0;
        return 1
                + getSubTree(left, right, left[node])
                + getSubTree(left, right, right[node]);
    }

}
