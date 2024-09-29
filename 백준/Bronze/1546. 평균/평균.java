import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        double max_val = 0;
        // N 길이의 점수 배열 선언
        double[] points = new double[N];
        // 그리고 배열에 값들 입력
        for (int i = 0; i < N; i++) {
            double cur_val = scan.nextInt();
            points[i] = cur_val;
            if (cur_val > max_val) {
                max_val = cur_val;
            }
        }
        max_val /= 100.0;
        double result = 0;
        for (double point : points){
            result += point / max_val;
        }
        result /= N;
        System.out.println(result);


    }
}
