import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();

        for (int tc = 1; tc <= n; tc++) {
            HashSet<Character> countSet = new HashSet<>();

            String stringNumber = br.readLine();
            int multiplyNumber = Integer.parseInt(stringNumber);
            int mNum = 1;
            while (countSet.size() < 10) {
                stringNumber =  String.valueOf(multiplyNumber * mNum);
                mNum++;
                for (int i = 0; i < stringNumber.length(); i++) {
                    countSet.add(stringNumber.charAt(i));
                }
            }

            sb.append("#" + tc + " " + stringNumber + "\n");
        }
        System.out.println(sb.toString().trim());

    }
}