import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 1; i <= T; i++) {
            int changeNum = 0;
            String input = br.readLine();
            String[] memory = input.split("");

            // 역발상 : 모든 걸 0으로
            for (int j = 0; j < memory.length; j++) {
                if (memory[j].equals("0")) {
                    continue;
                }
                for (int k = j; k < memory.length; k++) {
                    if (memory[k].equals("1")) {
                        memory[k] = "0";
                    } else {
                        memory[k] = "1";
                    }
                }
                changeNum++;

            }
            System.out.println("#"+i+" "+changeNum);
        }

    }
}
