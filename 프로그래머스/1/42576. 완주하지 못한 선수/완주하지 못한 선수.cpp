#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map<string, int> pass;
    for (int i = 0; i < participant.size(); i++) {
        pass[participant[i]]++;
    }
    for (int i = 0; i < completion.size(); i++) {
        pass[completion[i]]--;
    }
    
    for (const auto& [k, v] : pass) {
        if (v == 1) {
            return k;
        }
    }
}