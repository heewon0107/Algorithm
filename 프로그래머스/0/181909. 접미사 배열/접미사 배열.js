function solution(my_string) {
    let answer = []
    for (i = 0; i < my_string.length; i++) {
        answer = [...answer, my_string.substring(i)];
    }
    return answer.sort();
}