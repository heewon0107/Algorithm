#include <iostream>
// memset
#include <string.h>
using namespace std;

// 우 하 좌 상
int dr[4] = {0, 1, 0, -1};
int dc[4] = {1, 0, -1, 0};
int arr[101][101];

int main(){
    int M, N;
    cin >> M >> N;
    memset(arr, 0, sizeof(arr));


    // Result
    int result = 0;
    int cnt = 1;
    // Position
    int d = 0;
    int r = 0;
    int c = 0;
    arr[r][c] = 1;

    // If not Destination
    while (1) {
        if (cnt == M*N) break;
        // Move
        int nr = r + dr[d];
        int nc = c + dc[d];
        // Valid Check
        if (nr < 0 || nr >= M || nc < 0 || nc >= N || arr[nr][nc] == 1) {
            result++;
            d = (d+1) % 4;
        } else {
            arr[nr][nc] = 1;
            r = nr;
            c = nc;
            cnt++;
        }
    }

    cout << result;
    return 0;
}