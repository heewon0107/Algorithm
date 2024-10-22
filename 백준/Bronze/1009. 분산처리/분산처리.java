import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        Map<Integer, List<Integer>> map = new HashMap<>();

        map.put(2, Arrays.asList(2,4,8,6));
        map.put(3, Arrays.asList(3,9,7,1));
        map.put(4, Arrays.asList(4,6,4,6));
        map.put(7, Arrays.asList(7,9,3,1));
        map.put(8, Arrays.asList(8,4,2,6));
        map.put(9, Arrays.asList(9,1,9,1));

        for (int i = 0; i < N; i++) {
            StringTokenizer st  = new StringTokenizer(br.readLine());
            String a = st.nextToken();
            int new_a = Character.getNumericValue(a.charAt(a.length() - 1));
            if (new_a == 1 || new_a == 5 || new_a == 6) {
                System.out.println(new_a);
                continue;
            } else if (new_a == 0) {
                System.out.println(10);
                continue;
            }
            int b = (Integer.parseInt(st.nextToken()) - 1) % 4 ;
            System.out.println(map.get(new_a).get(b));
        }
    }
}
