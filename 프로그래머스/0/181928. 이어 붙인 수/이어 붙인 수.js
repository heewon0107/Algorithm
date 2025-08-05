function solution(num_list) {
    let hol = "";
    let jjak = "";
    
    for (const num of num_list) {
        num % 2 == 0 ? jjak += num : hol += num;
    }    
    return parseInt(hol) + parseInt(jjak);
}