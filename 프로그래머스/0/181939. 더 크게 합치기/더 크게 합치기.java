class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String first = String.valueOf(a);
        String second = String.valueOf(b);
        int one = Integer.parseInt(first + second);
        int two = Integer.parseInt(second + first);
        
        answer = one > two ? one : two;
        return answer;
    }
}