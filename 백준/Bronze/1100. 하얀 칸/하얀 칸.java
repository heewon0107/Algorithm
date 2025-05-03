import java.io.*;

class Main{
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int result = 0;
        for (int i = 0; i < 8; i++) {
            String line = br.readLine();
            for (int j = 0; j < line.length(); j++) {
                if ((i % 2 == 0 && j % 2 == 0) || (i % 2 == 1 && j % 2 == 1)) {
                    if (line.charAt(j) == 'F') {
                        result++;
                    }
                }
                
            }
        }
        System.out.println(result);
        
    }
}