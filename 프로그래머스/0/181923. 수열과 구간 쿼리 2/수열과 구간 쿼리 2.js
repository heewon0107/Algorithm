function solution(arr, queries) {
    var answer = [];
    queries.forEach((e) => {
        const start = e[0];
        const end = e[1];
        const k = e[2];
        
        let val = 1e9;
        for (i=start; i <= end; i++) {
            const tar_num = arr[i];
            // k < tar_num 중 가장 작은 값.
            if (k < tar_num) {
                val = Math.min(tar_num, val);
            }
        }
        val = val === 1e9 ? -1 : val;
        answer.push(val);
        
    })
    
    return answer;
}