function solution(a, d, included) {
    var answer = 0;
    for (const tf of included) {
        if (tf) answer += a;
        a += d;
    }
    return answer;
}