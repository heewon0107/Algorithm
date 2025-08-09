function solution(players, m, k) {
    var cnt = 0;
    // server 개수와 시간 관리
    let server = [];
    let available_people_time;
    players.forEach((num) => {
        // 사람 수
        available_people_time = (server.length + 1) * m;
        // 현재 가용할 수 있는 사람보다 많이 들어온다.
        // 서버 증축 하자.
        if (num >= available_people_time) {
            const addServerAmount = Math.floor((num - available_people_time + m) / m); 
            cnt += addServerAmount;
            for (i=0; i<addServerAmount; i++) {
                server.push(k);
            }            
        } 
        // 서버 시간 정산
        for (i=0; i<server.length; i++) {
            server[i]--;
        }
        // 다 쓴 서버 반납
        while (server.length && !server[0]) {
            server.shift();
        }
    })
    
    return cnt;
}