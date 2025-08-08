const delta = [[0,-1], [1,0], [0,1], [-1,0]];

function solution(maps) {
    const set = new Set()
    const m = maps[0].length;
    const n = maps.length;
    
    const visited = Array.from({length: n}, () => Array(m).fill(false));
    const queue = [];
    queue.push([0,0,1])
    visited[0][0] = true;
    
    function isValidate(r, c) {
        return r >= 0 && r < n && c >= 0 && c < m && maps[r][c] === 1;
    }
    
    while (queue.length) {
        const [r, c, cnt] = queue.shift();
        
        if (r === n - 1 && c === m - 1) {
            return cnt;
        }
        
        for (const d of delta) {
            const nr = r + d[0];
            const nc = c + d[1];
            if (isValidate(nr, nc) && !visited[nr][nc]) {
                queue.push([nr, nc, cnt + 1])
                visited[nr][nc] = true;
            }
        }
    }
    return -1;
}




