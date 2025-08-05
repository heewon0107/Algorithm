function solution(my_string, is_suffix) {
    var answer = 0;
    const my_len = my_string.length;
    const su_len = is_suffix.length;
    if (my_len < su_len) return answer;
        
    my_string.substring(my_len - su_len) == is_suffix ? answer = 1 : true; 
    
    
    return answer;
}