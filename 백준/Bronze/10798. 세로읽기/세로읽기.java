import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] vocas = new String[5];
        int maxLength = 0;
        for (int i = 0; i < 5; i++) {
            vocas[i] = br.readLine();
            if (vocas[i].length() > maxLength) {
                maxLength = vocas[i].length();
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int col = 0; col < maxLength; col++) {
            for (int row = 0; row < 5; row++) {
                // 현재 순회하는 열의 길이가 없다면
                if (vocas[row].length() <= col) {
                    continue;
                }
                sb.append(vocas[row].charAt(col));
            }
        }
        System.out.println(sb.toString());

    }
}
