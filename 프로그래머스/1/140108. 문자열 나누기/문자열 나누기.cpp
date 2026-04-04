#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = 0;
    int i = 0;
    
    while (i < s.size()) {
        char x = s[i];
        int same = 1;
        int other = 0;
        
        while (same != other) {
            i++;
            if (i == s.size()) break;
            
            if (x == s[i]) {
                same++;
            } else {
                other++;
            }
        }
        answer++;
        i++;
        
        
    }
    return answer;
}