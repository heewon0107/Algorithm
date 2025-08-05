function solution(my_string, index_list) {
    var answer = '';
    for (const val of index_list) {
        answer += my_string.charAt(val)
    }
    return answer;
}