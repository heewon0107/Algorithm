function solution(ineq, eq, n, m) {
    var answer = 0;
    if (eq == "!") {
        answer = ineq == "<" ? n < m : n > m 
    } else {
        answer = ineq == ">" ? n >= m : n <= m 
    }
    return answer ? 1 : 0;
}