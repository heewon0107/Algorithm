import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < 3; i++) {
            int cnt = 0;
            for (int j = 0; j < 4; j++) {
                int cur = sc.nextInt();
                if (cur == 0) {
                    cnt++;
                }
            }
            char result = 'a';
            switch (cnt) {
                case 0:
                    result = 'E';
                    break;
                case 1:
                    result = 'A';
                    break;
                case 2:
                    result = 'B';
                    break;
                case 3:
                    result = 'C';
                    break;
                case 4:
                    result = 'D';
                    break;


            }
            System.out.println(result);
        }
    }

}
