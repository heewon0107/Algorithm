function solution(numbers, n) {
    var answer = 0;
    numbers.map(x => answer <= n ? answer += x : true);
    return answer;
}