function solution(s){
    const stack = [];
    for (let i = 0; i < s.length; i++) {
        
        if (s.charAt(i) === "(") {
           stack.push("hi"); 
        } else {
            if (stack.length) {
                stack.pop()
            } else {
                return false;
            }
        }
    }
    return stack.length ? false : true;
}