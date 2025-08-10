function solution(n, times) {
    // 심사 시간 정렬
    times.sort((a, b) => a - b);
    let left = 0;
    let right = times[times.length - 1] * n;
    var answer = 0;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        let complete = 0;
        for (i=0; i<times.length; i++) {
            complete += Math.floor(mid / times[i]);
        }
        if (complete < n) {
            left = mid + 1;
        } else {
            right = mid - 1;
            answer = mid;
        }
    }
    return answer;
}