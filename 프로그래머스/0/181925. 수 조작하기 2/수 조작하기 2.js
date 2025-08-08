function solution(numLog) {
    var answer = '';
    for (i=0; i < numLog.length; i++) {
        // 뒤에서 앞을 빼
        switch (numLog[i] - numLog[i - 1]) {
            case 1: answer += "w"; break;
            case -1: answer += "s"; break;
            case 10: answer += "d"; break;
            case -10: answer += "a"; break;
        }
    }
    return answer;
}