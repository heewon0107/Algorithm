import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int x,y,w,h;
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());
        w = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());

        int minDistance = 1000;
        if (x >= (float) w/2) {
            minDistance = w-x;
        } else {
            minDistance = x;
        }

        if (y >= (float) h/2) {
            minDistance = Math.min(minDistance, h-y);
        } else {
            minDistance = Math.min(minDistance,y);
        }


        System.out.println(minDistance);
        br.close();
    }
}
