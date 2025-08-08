function solution(l, r) {
    const answer = [];
    const queue = ["5"];

    while (queue.length) {
        const num = queue.shift();
        const curr = Number(num);
        
        if (curr > r) continue;
        
        if (curr >= l) answer.push(curr);
        
        queue.push(num + "5");
        queue.push(num + "0");
        
    }
    
    return answer.length ? answer.sort((a, b) => a - b) : [-1];
}