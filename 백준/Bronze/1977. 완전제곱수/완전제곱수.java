import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m, n;
        m = sc.nextInt();
        n = sc.nextInt();
        int firstNum = (int) Math.sqrt(n);
        int result = 0;
        int value = firstNum*firstNum;
        while (value >= m) {
            result += value;
            firstNum--;
            value = firstNum*firstNum;
        }
        firstNum++;
        value = firstNum*firstNum;
        if (result==0) {
            System.out.println(-1);
        }else{
        System.out.println(result);
        System.out.println(value);
        }
    }

}