import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String alphabet = br.readLine();
        int[] locationOfAlpha = new int[26];
        for (int i = 0; i < 26; i++) {
            locationOfAlpha[i] = -1;
        }

        for (int i = 0; i < alphabet.length(); i++) {
            int currentAlphabet = alphabet.charAt(i) - 97;
            // 이미 해당 알파벳이 이전에 있었다.
            if (locationOfAlpha[currentAlphabet] != -1) {
                continue;
            }
            locationOfAlpha[currentAlphabet] = i;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 26; i++) {
            sb.append(locationOfAlpha[i]).append(" ");
        }
        System.out.println(sb.toString().trim());
    }
}
