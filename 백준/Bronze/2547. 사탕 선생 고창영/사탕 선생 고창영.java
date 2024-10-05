import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        String[] result = new String[n];
        for (int i = 0; i < n; i++) {
            BigInteger candy_sum = BigInteger.ZERO;
            sc.nextLine();
            long candy_num = sc.nextLong();
            sc.nextLine();
            for (int j = 0; j < candy_num; j++) {
                BigInteger candy = new BigInteger(sc.nextLine());
                candy_sum = candy_sum.add(candy);
            }
            BigInteger num = BigInteger.valueOf(candy_num);
            if (candy_sum.mod(num).compareTo(BigInteger.ZERO) == 0 ) {
                result[i] = "YES";
            }
            else {
                result[i] = "NO";

            }

        }
        sc.close();
        for (String s : result) {
            System.out.println(s);
        }
    }

}