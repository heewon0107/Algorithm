import java.util.Scanner;


public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float result = 0;
        float score_sum = 0;
        for (int i = 0; i < 20; i++) {
            String delete = sc.next();
            float score = sc.nextFloat(); // 학점
            String grade = sc.next(); // 과목 평점
            // 학점이 P면 계산 제외
            if (grade.equals("P")) {
                continue;
                // F면 학점에만
            } else if (grade.equals("F")) {
                score_sum += score;
            }else {
                float point = 0;
                switch (grade){
                    case "A+" : point = 4.5f;
                        break;
                    case "A0" : point = 4.0f;
                        break;
                    case "B+" : point = 3.5f;
                        break;
                    case "B0" : point = 3.0f;
                        break;
                    case "C+" : point = 2.5f;
                        break;
                    case "C0" : point = 2.0f;
                        break;
                    case "D+" : point = 1.5f;
                        break;
                    case "D0" : point = 1.0f;
                }
                result += point * score;
                score_sum += score;
            }

        }
        result /= score_sum;
        System.out.println(result);
        sc.close();
    }

}

