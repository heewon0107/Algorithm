import java.io.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int len = str.length();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < len; i++) {
            char chr = str.charAt(i);
            
            if (chr > 92) { // if small
                sb.append(Character.toUpperCase(chr));
            } else {
                sb.append(Character.toLowerCase(chr));           
            }
        }
        System.out.println(sb);
        
    }
}