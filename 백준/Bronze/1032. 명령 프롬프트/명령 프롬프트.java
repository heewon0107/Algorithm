import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            String name = br.readLine();
            if (i == 0) {
                sb.append(name);
                continue;
            }
            for (int j = 0; j < name.length(); j++) {
                if (sb.charAt(j) != name.charAt(j)) {
                    sb.replace(j, j+1, "?");
                }
            }
        }
        System.out.println(sb.toString().trim());


    }
}