import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException {
        Map<String, Integer> dictionary = new HashMap<>();
        dictionary.put("black", 1);
        dictionary.put("brown", 10);
        dictionary.put("red", 100);
        dictionary.put("orange", 1_000);
        dictionary.put("yellow", 10_000);
        dictionary.put("green", 100_000);
        dictionary.put("blue", 1_000_000);
        dictionary.put("violet", 10_000_000);
        dictionary.put("grey", 100_000_000);
        dictionary.put("white", 1_000_000_000);

        Map<String, String> val = new HashMap<>();
        val.put("black", "0");
        val.put("brown", "1");
        val.put("red", "2");
        val.put("orange", "3");
        val.put("yellow", "4");
        val.put("green", "5");
        val.put("blue", "6");
        val.put("violet", "7");
        val.put("grey", "8");
        val.put("white", "9");

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String value1 = br.readLine();
        String value2 = br.readLine();
        String last = br.readLine();
        String result;
        result = val.get(value1) + val.get(value2);
        long new_result = Integer.parseInt(result);

        System.out.print(new_result * dictionary.get(last));
        br.close();

    }
}