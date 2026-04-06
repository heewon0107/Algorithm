#include <string>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;



string solution(int a, int b) {
    string answer = "";
    // day_diff % 7
    unordered_map<int, string> day;
    day[0] = "FRI";
    day[1] = "SAT";
    day[2] = "SUN";
    day[3] = "MON";
    day[4] = "TUE";
    day[5] = "WED";
    day[6] = "THU";

    // Day per Month
    vector<int> m_to_d(13, 0);
    for (int i = 1; i < 13; i++) {
        if (i == 1 || i == 3 || i == 5 || i == 7 || i == 8 || i == 10 || i == 12 ) {
            m_to_d[i] = 31;
        } else if (i == 2){
            m_to_d[i] = 29;
        } else {
            m_to_d[i] = 30;
        }
    }
    // total_day
    int total = -1;
    for (int i = 0; i < a; i++) {
        total += m_to_d[i];
    }
    total += b;
    return day[total % 7];
}