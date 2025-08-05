function solution(my_strings, parts) {
    var answer = '';
    let i = 0;
    for (const val of parts) {
        answer += my_strings[i].substring(val[0], val[1] + 1);
        i++;
    }
    return answer;
}