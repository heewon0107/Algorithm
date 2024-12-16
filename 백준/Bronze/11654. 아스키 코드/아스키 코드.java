import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String character = br.readLine();
        char[] chars = character.toCharArray();
        System.out.println(chars[0]+0);

    }
}
