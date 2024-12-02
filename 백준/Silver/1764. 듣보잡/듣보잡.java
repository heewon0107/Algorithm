import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        Set<String> nameHear = new HashSet<>();
        Set<String> nameLook = new HashSet<>();
        for (int i = 0; i < N; i++) {
            nameHear.add(br.readLine());
        }
        int result = 0;
        List<String> resultNames = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            String vocabulary = br.readLine();
            if (nameLook.contains(vocabulary)) {
                continue;
            }
            nameLook.add(vocabulary);
            if (nameHear.contains(vocabulary)) {
                resultNames.add(vocabulary);
                result++;

            }
        }
        Collections.sort(resultNames);
        StringBuilder sb = new StringBuilder();
        sb.append(result).append("\n");
        for (String resultName : resultNames) {
            sb.append(resultName).append("\n");
        }
        System.out.println(sb.toString().trim());
    }
}
