function solution(a, b, c) {
    var answer = 0;
    
    // Different all
    if (a !== b && b !== c) answer = a + b + c;
    if (!(a === b && b === c) && (a === b | b === c | a === c) ) answer = (a + b + c) * (a * a + b * b + c * c);
    // Same all value
    if (a === b && b === c) answer = (a + b + c) * (a * a + b * b + c * c) * (a * a * a + b * b * b + c * c * c);
    
    return answer;
}