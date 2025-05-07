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
            int N = Integer.parseInt(br.readLine());
            int distance = 0;
            int velocity = 0;
            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int command = Integer.parseInt(st.nextToken());
                switch (command) {
                    case 1:
                        velocity += Integer.parseInt(st.nextToken());
                        break;
                    case 2:
                        velocity -= Integer.parseInt(st.nextToken());
                        if (velocity < 0) {
                            velocity = 0;
                        }
                        break;
                }
                distance += velocity;
            }
            sb.append("#" + tc + " " + distance).append("\n");
        }
        System.out.println(sb.toString());
    }

}
