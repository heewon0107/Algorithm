import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        sc.nextLine();
        int num = n * m;
        int result = num - 1;

        System.out.println(result);
        sc.close();
    }

}
