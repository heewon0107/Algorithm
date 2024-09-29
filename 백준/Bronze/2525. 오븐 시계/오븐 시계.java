import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a, b, c;
        a = scan.nextInt();
        b = scan.nextInt();
        c = scan.nextInt();
        // b에 1000이하의 시간이 더해짐.
        
        b += c; // 분
        
        while (b >= 60){
            b -= 60;
            a += 1;
        }
        while (a >= 24){
            a -= 24;
            }
        System.out.println(a + " " + b);
    }
}