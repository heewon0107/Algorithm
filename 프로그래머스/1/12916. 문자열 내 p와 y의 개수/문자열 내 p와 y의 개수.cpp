#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    int p = 0, y = 0;
    int N = s.size();
    
    for (int i = 0; i < N; i++) {
        if (s[i] == 'P' || s[i] == 'p') {
            p++;
        } else if (s[i] == 'Y' || s[i] == 'y') {
            y++;
        }
    }
    cout << p << y;
    if (p == y) return true;
    else return false;
}