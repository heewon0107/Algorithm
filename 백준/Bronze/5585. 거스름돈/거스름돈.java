import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    static int theRest;
    static int result = 0;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        theRest = 1000 - Integer.parseInt(br.readLine());
        greedy(500);
        greedy(100);
        greedy(50);
        greedy(10);
        greedy(5);
        greedy(1);
        System.out.println(result);
    }

    static void greedy(int price) {
        while (theRest >= price) {
            result++;
            theRest -= price;
        }
    }
}
