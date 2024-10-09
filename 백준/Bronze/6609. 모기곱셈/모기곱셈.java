import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S;
        while ((S = br.readLine()) != null){
            StringTokenizer st = new StringTokenizer(S);
            int m, p, l, e, r, s, n;
            m = Integer.parseInt(st.nextToken()); // 모기 ex)10
            p = Integer.parseInt(st.nextToken()); // 번데기 ex)20
            l = Integer.parseInt(st.nextToken()); // 유충 ex)40
            e = Integer.parseInt(st.nextToken()); // 한 모기가 낳는 알 수 ex)4
            r = Integer.parseInt(st.nextToken()); // 살아남는 유충 비율 ex)2
            s = Integer.parseInt(st.nextToken()); // 살아남는 번데기 비율 ex)2
            n = Integer.parseInt(st.nextToken()); // 우리가 모기 수를 구하려는 시점. (N주 후) ex)10
            // 모기가 알 낳고 죽음.
//            l += m * e; // 바로 유충에 합해줌.
            int week = 0;
            while (week < n) {
                week++;
                int new_m = (int) p / s; // p개의 번데기 중 s 번째들만 모기
                int new_l = (int) m * e; // 성충모기는 바로 알낳고 사망.
                int new_p = (int) l / r; // l개의 유충중 r 번째들만 번데기
                m = new_m;
                l = new_l;
                p = new_p;
            }
            System.out.println(m);
        }

        br.close();
    }

}
