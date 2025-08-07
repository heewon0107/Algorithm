function solution(code) {
    var answer = '';
    let mode = 0;
    for (i=0; i<code.length; i++) {
        if (code.charAt(i) == "1") {
            mode = (mode + 1) % 2;
            continue;
        }
        if (mode == 0 && i % 2 == 0) {
            answer += code.charAt(i);
        }
        if (mode == 1 && i % 2 == 1) {
            answer += code.charAt(i);
        }
    }
    
    answer = answer == '' ? "EMPTY" : answer;
    
    return answer;
}