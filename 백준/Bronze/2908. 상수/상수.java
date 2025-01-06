import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String firstNumber = st.nextToken();
        String secondNumber = st.nextToken();
        String firstNumberReversed = new StringBuffer(firstNumber).reverse().toString();
        String secondNumberReversed = new StringBuffer(secondNumber).reverse().toString();

        if (firstNumberReversed.compareTo(secondNumberReversed) > 0) {
            System.out.println(firstNumberReversed);
        } else {
            System.out.println(secondNumberReversed);
        }


    }
}
