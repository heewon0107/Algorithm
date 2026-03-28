#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>
using namespace std;



vector<vector<int>> solution(vector<vector<int>> data, string ext, int val_ext, string sort_by) {
    // 탬플릿 생성
    unordered_map<string, int> dict;
    dict["code"] = 0;
    dict["date"] = 1;
    dict["maximum"] = 2;
    dict["remain"] = 3;
    
    int idx = dict[ext];
    
    vector<vector<int>> answer;
    // 1. ext < val_ext 데이터 추출
    for (int i = 0; i < data.size(); i++) {
        if (data[i][idx] < val_ext) {
            answer.push_back(data[i]);
        }
    }
    idx = dict[sort_by];
    // 2. sort_by 오름차순 정렬
    sort(answer.begin(), answer.end(), [&](auto &a, auto&b) {
        return a[idx] < b[idx];
    });
    
    return answer;
}