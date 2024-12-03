import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Set<String> users = new HashSet<>();
        int N = Integer.parseInt(br.readLine());
        final String NO = "ENTER";
        int result = 0;
        for (int num = 0; num < N; num++) {
            String str = br.readLine();
            if (str.equals(NO)) {
                users.clear();
                continue;
            }
            if (!users.contains(str)) {
                users.add(str);
                result++;
            }
        }
        System.out.println(result);

    }
}
