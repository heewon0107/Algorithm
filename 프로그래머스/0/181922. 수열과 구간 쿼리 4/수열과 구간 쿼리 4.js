function solution(arr, queries) {
    queries.forEach((e) => {
        const s = e[0];
        const end = e[1];
        const k = e[2];
        
        for (i=s; i<=end; i++) {
            i % k === 0 ? arr[i]++ : true;
        }
    })
    return arr;
}