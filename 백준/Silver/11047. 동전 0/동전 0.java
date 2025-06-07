import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int theRest;
    static int result = 0;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        theRest = Integer.parseInt(st.nextToken());

        int[] coinValue = new int[n];

        for (int i = coinValue.length - 1; i >= 0 ; i--) {
            coinValue[i] = Integer.parseInt(br.readLine());
        }

        for (int coin : coinValue) {
            greedy(coin);
        }
        System.out.println(result);
    }

    static void greedy(int price) {
        while (theRest >= price) {
            result++;
            theRest -= price;
        }
    }
}
