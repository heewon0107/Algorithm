import java.util.Scanner;


public class Main {
    private static int result = 0;

    public static void fire(int total, int idx, int N, int[] daily, int[] prices) {
        total += prices[idx];
        idx += daily[idx];
        if (idx == N) {
            if (total > result) {
                result = total;
            }
            return;
        }
        if (idx >= N) {
            return;
        } else {
            if (total > result) {
                result = total;
            }
            for (int i = idx; i < N; i++) {

                fire(total, i, N, daily, prices);
            }


        }

    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int[] daily = new int[N];
        int[] prices = new int[N];
        for (int i = 0; i < N; i++) {
            daily[i] = scan.nextInt();
            prices[i] = scan.nextInt();
        }

        for (int i = 0; i < N; i++) {
            fire(0, i, N, daily, prices);
        }
        System.out.println(result);

    }
}
