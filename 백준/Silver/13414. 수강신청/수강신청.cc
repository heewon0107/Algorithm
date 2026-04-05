#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main() {
    int K, L;
    cin >> K >> L;
    
    // 수강신청 해쉬
    unordered_map<string, int> apply;
    for (int i = 0; i < L; i++) {
        string num;
        cin >> num;
        apply[num] = i;
    }
    // 벡터로 변경
    vector<pair<string, int>> lst(apply.begin(), apply.end());
    
    // 정렬
    sort(lst.begin(), lst.end(), [](auto &a, auto &b) {
        return a.second < b.second;
    });
    
    // K만큼 출력
    for (int i = 0; i < K; i++) {
        if (lst.size() <= i) break;
        cout << lst[i].first << "\n";
    }
    
    return 0;
}