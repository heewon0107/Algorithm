import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int tc = 1; tc <= n; tc++) {
            boolean[] numberCheck = new boolean[10];
            String stringNumber = br.readLine();
            int multiplyNumber = Integer.parseInt(stringNumber);
            int multiplyCount = 1;
            while (true) {
                stringNumber = multiply(multiplyNumber, multiplyCount++);

                for (int i = 0; i < stringNumber.length(); i++) {
                    numberCheck[stringNumber.charAt(i) - '0'] = true;
                }
                // if allCheck, break!
                boolean allChecked = true;
                for (boolean check : numberCheck) {
                    if (!check) {
                        allChecked = false;
                        break;
                    }
                }
                if (allChecked) break;
            }



            sb.append("#" + tc + " " + stringNumber + "\n");
        }
        System.out.println(sb.toString().trim());

    }
    public static String multiply(int target, int n) {
        return String.valueOf(target * n);
    }
}