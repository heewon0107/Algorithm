function solution(n, k) {
    var answer = [];
    for (i=1; i<=n/k; i++) {
        answer = [...answer, i*k]
    }
    return answer;
}