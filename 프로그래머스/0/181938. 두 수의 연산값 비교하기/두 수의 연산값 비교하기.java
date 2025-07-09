class Solution {
    public int solution(int a, int b) {
        // int answer = 0;
        int aPlusB = Integer.parseInt(String.valueOf(a) + String.valueOf(b));
        int aMultiplyB = 2 * a * b;
        
        
        
        return aPlusB < aMultiplyB ? aMultiplyB : aPlusB;
    }
}