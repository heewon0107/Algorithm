import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
//        int N = Integer.parseInt(st.nextToken()); // 기타줄의 개수
//        int M = Integer.parseInt(st.nextToken()); // 브랜드의 개수
//        int result = 1000;
//        int one = 1000;
//        int pack = 1000;
//        for (int i = 0; i < M; i++) {
//            StringTokenizer he = new StringTokenizer(br.readLine());
//            int pack_ = Integer.parseInt(he.nextToken());
//            int one_ = Integer.parseInt(he.nextToken());
//            pack = Math.min(pack_,pack);
//            one = Math.min(one_, one);
//        }
//        int one_price = one * N;
//
//        System.out.println(result);
        System.out.println(Integer.parseInt(st.nextToken()) - Integer.parseInt(st.nextToken()));

        br.close();
    }

}
