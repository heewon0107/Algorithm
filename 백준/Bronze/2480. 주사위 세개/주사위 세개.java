import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Set<Integer> sameNumbers = new HashSet<>();
        int sameNum = 0;
        while (st.hasMoreTokens()) {
            int Num = Integer.parseInt(st.nextToken());
            if (sameNumbers.contains(Num)) {
                sameNum = Num;
            }
            sameNumbers.add(Num);
        }
        int result = 0;
        switch (sameNumbers.size()) {
            case 1: result = 10000 + 1000 * sameNum; break;
            case 2: result = 1000 + 100 * sameNum; break;
            default: result = Collections.max(sameNumbers) * 100;
        }
        System.out.println(result);

    }
}
