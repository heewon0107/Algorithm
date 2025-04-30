import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long N = Long.parseLong(br.readLine());
        int F = Integer.parseInt(br.readLine());

        long base = (N / 100) * 100;

        for (int i = 0; i < 100; i++) {
            if ((base + i) % F == 0) {
                System.out.printf("%02d", i);
                break;
            }
        }
    }

}
