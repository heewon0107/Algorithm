import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int price = Integer.parseInt(br.readLine());
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            if (price <= 0) {
                break;
            }
            StringTokenizer st = new StringTokenizer(br.readLine());
            price -= Integer.parseInt(st.nextToken()) * Integer.parseInt(st.nextToken());
        }
        if (price == 0) {System.out.println("Yes");}
        else {System.out.println("No");}
    }
}
